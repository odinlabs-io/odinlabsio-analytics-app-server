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

import argparse
import importlib
import sys

import pandas as pd

from app.batch.to_parquet import to_parquet, generate_schema
from app.db import parquet_schema

parser = argparse.ArgumentParser()

parser.add_argument('--csv', help='csv file path')
parser.add_argument('--settings', help='env configuration file')
parser.add_argument('--generate-schema', help='override schema and infer schema from data', action="store_true",
                    default=False)


def dict_from_module(module):
    context = {}
    for setting in dir(module):
        # you can write your filter here
        if setting.isupper() and setting.isascii():
            context[setting] = getattr(module, setting)

    return context


def run(args: argparse.Namespace):
    if args.csv is None:
        pass
    else:
        df = pd.read_csv(args.csv)
        settings = importlib.import_module(args.settings)

        settings = dict_from_module(settings)

        if not args.generate_schema:
            schema = parquet_schema.build(settings['PARQUET_DATA_SET_NAME'],
                                          settings['DATA_ROOT_DIR'] + '/' + settings['PARQUET_SCHEMA_FILE'])['schema']
            to_parquet(df=df, schema=schema, **settings)
        else:
            to_parquet(df=df, **settings)
            generate_schema(**settings)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('--csv', help='csv file path')
    parser.add_argument('--settings', help='env configuration file')
    parser.add_argument('--generate-schema', help='override schema and infer schema from data', action="store_true",
                        default=False)

    run(parser.parse_args(sys.argv[1:]))
