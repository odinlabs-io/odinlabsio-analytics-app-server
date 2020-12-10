#  MIT License
#
#  Copyright (c) 2020 OdinLabs IO
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

from typing import List, Tuple

import pandas as pd

from app.aggregation import filter_dag, aggregation_dag, pyarrow_eval_factory, pandas_eval_factory
from app.db import ParquetDataSource


class Aggregation:
    def __init__(self, parquet_data_source: ParquetDataSource):
        self._filter_eval_factory = pyarrow_eval_factory()
        self._eval_factory = pandas_eval_factory()
        self._parquet_data_source = parquet_data_source

    def get_aggregate(self, data_set_name: str, filters: List[str], aggregates: List[Tuple[str, str]],
                      dimensions: List[Tuple[str, str]]):
        """

        :param data_set_name:
        :param filters:
        :param aggregates: label, value list
        :param dimensions: label, value list
        :return: groupby df
        """
        aggregate_computers = [
            (aggr_name, self._eval_factory.evaluator('aggregationStatement').build(0, aggregation_dag(aggr))) for
            aggr_name, aggr in aggregates]

        if len(filters) > 0:
            if len(filters) > 1:
                analytic_filter = filter_dag('AND'.join(filters))
            else:
                analytic_filter = filter_dag(filters[0])

            filter_condition = self._filter_eval_factory.evaluator('conditionStatement').build(0, analytic_filter)
        else:
            filter_condition = None

        dimensions = [dimension for _, dimension in dimensions]
        if filter_condition:
            columns = dimensions + filter_condition.input_columns() + [variable for _, aggr in aggregate_computers
                                                                       for
                                                                       variable
                                                                       in aggr.input_columns()]
            df = self._parquet_data_source.get_data_set(data_set_name) \
                .to_table(columns=list(set(columns)),
                          filter=filter_condition()).to_pandas()
        else:
            columns = dimensions + [variable for _, aggr in aggregate_computers
                                    for
                                    variable
                                    in aggr.input_columns()]
            df = self._parquet_data_source.get_data_set(data_set_name) \
                .to_table(columns=list(set(columns))).to_pandas()

        index = [emitted_column for aggregate in aggregate_computers for emitted_column in aggregate[1].emit_columns()]
        index = list(set(index))

        def compute_aggregates(sub_df):
            computed_aggregates = {}
            for name, aggregate in aggregate_computers:
                computed_aggregates[name] = aggregate(sub_df, index)

            return pd.DataFrame(computed_aggregates)

        df = df.groupby(dimensions).apply(compute_aggregates)

        if len(index) > 0:
            return df
        else:
            index = df.index
            df.index = index.droplevel(len(index.names) - 1)

            return df
