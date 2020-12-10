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
import logging
import os.path as osp
import pickle
from collections import defaultdict
from typing import List, Dict

import pyarrow as pa


def is_measure(col):
    col_type = col[1]

    return col_type == pa.int64() or col_type == pa.int32() or col_type == pa.float64() or col_type == pa.float32() or col_type == pa.float16()


def is_category(col):
    return not is_measure(col)


"""
Append fields to schema
"""
add: Dict[str, List[pa.Field]] = defaultdict(list)

"""
Remove fields from schema
"""
remove: Dict[str, List[str]] = defaultdict(list)


def build(data_set_name: str, schema_file: str):
    """
    Original schema can be loaded from pickle file.
    The initial schema can be generated with schema = pa.Schema.from_pandas(df)
    If none it will create an empty schema and use add field to create schema based on properties only
    """
    logging.info('Loading schema file for data set {} from {}'.format(data_set_name, schema_file))

    if osp.isfile(schema_file):
        schema = pickle.load(open(schema_file, 'rb')) if osp.isfile(schema_file) else {}

        partitions = schema['partitions']
        schema = schema['schema']

        for field in remove[data_set_name]:
            schema = schema.remove(schema.get_field_index(field))

        for field in add[data_set_name]:
            schema = schema.append(field)

        """
        Used by dashboard service to collect data set fields
        """
        columns = []
        measures = []
        categories = []

        for column_name, column_type in zip(schema.names, schema.types):
            columns.append({'name': column_name})
            if is_measure((column_name, column_type)):
                measures.append({'name': column_name})
            if is_category((column_name, column_type)):
                categories.append({'name': column_name})

        return {
            'schema': schema,
            'partitions': partitions,
            'columns': columns,
            'measures': measures,
            'categories': categories
        }
    else:
        error = 'Schema file {} not found'.format(schema_file)

        raise Exception(error)
