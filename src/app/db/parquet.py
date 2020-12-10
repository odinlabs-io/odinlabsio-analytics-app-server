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

import pyarrow.dataset as ds
from flask import Flask

from app.db import parquet_schema


class ParquetDataSource:
    def __init__(self):
        self._properties = {}
        self._ds = {}
        self._sources = []

    def init_app(self, app: Flask):
        root_dir = app.config.get('DATA_ROOT_DIR')

        names = app.config.get('PARQUET_DATA_SET_NAMES')
        data_dirs = app.config.get('PARQUET_DATA_DIRS')
        schema_files = app.config.get('PARQUET_SCHEMA_FILES')

        for name, data_dir, schema_file in zip(names, data_dirs, schema_files):
            data_schema_file = root_dir + '/' + schema_file
            data_schema = parquet_schema.build(name, data_schema_file)
            data_file = root_dir + '/' + data_dir
            data_set = ds.dataset(data_file, format='parquet', schema=data_schema.get('schema'))

            self._properties[name] = data_schema
            self._ds[name] = data_set

        self._sources = names

    def get_schema(self, name: str):
        return self._properties[name].get('schema')

    def get_columns(self, name: str):
        return self._properties[name].get('columns')

    def get_measures(self, name: str):
        return self._properties[name].get('measures')

    def get_categories(self, name: str):
        return self._properties[name].get('categories')

    def get_data_set(self, name: str):
        return self._ds[name]

    def get_sources(self):
        return self._sources
