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

import os
import pickle

import pandas as pd
import pyarrow as pa
import pyarrow.dataset as ds
import pyarrow.parquet as pq


def to_parquet(df: pd.DataFrame, schema: pa.Schema = None, **kwargs):
    data_dir = kwargs['DATA_ROOT_DIR'] + '/' + kwargs['PARQUET_DATA_DIR']

    if not os.path.isdir(data_dir):
        os.makedirs(data_dir)

    partition_cols = kwargs.get('PARQUET_PARTITIONS')

    if partition_cols and len(partition_cols) > 0:
        # pyarrow removes partitions columns from df so we create partition columns and keep the initial data
        for col in partition_cols:
            p_column_name = 'p-' + col
            df[p_column_name] = df[col]
            if schema:
                col_idx = schema.get_field_index(col)
                field = schema.field(col_idx)

                schema.insert(col_idx + 1, pa.field(p_column_name, field.type, field.nullable, field.metadata))

        partition_cols = ['p-' + col for col in partition_cols]

    row_groups = kwargs.get('PARQUET_ROW_GROUPS')
    if row_groups and len(row_groups) > 0:
        df.sort_values(by=row_groups, inplace=True)

    table = pa.Table.from_pandas(df, schema=schema)
    pq.write_to_dataset(table, data_dir, partition_cols=partition_cols, use_legacy_dataset=False,
                        schema=schema)


def generate_schema(**kwargs):
    data_dir = kwargs['DATA_ROOT_DIR'] + '/' + kwargs['PARQUET_DATA_DIR']
    schema_file = kwargs['DATA_ROOT_DIR'] + '/' + kwargs['PARQUET_SCHEMA_FILE']

    partition_cols = kwargs.get('PARQUET_PARTITIONS')
    row_groups = kwargs.get('PARQUET_ROW_GROUPS')

    parquet = ds.dataset(data_dir, format='parquet')

    if os.path.isfile(schema_file):
        os.remove(schema_file)

    pickle.dump(
        {
            'schema': parquet.schema,
            'partitions':
                {
                    'columns': partition_cols,
                    'rows': row_groups
                }
        }, open(schema_file, "wb"))
