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

from flask import Flask

from app.db.mongo import MongoDataSource
from app.db.parquet import ParquetDataSource

mongo_data_source = MongoDataSource()

parquet_data_source = ParquetDataSource()


def init_app(app: Flask):
    auth = app.config.get('MONGO_AUTH_SOURCE')
    host = app.config.get('MONGO_HOST')
    user = app.config.get('MONGO_USER')
    db_name = app.config.get('MONGO_DB')

    app.config['MONGO_URI'] = 'mongodb://{}@{}/{}?authSource={}'.format(user, host, db_name, auth)

    mongo_data_source.init_app(app)
    parquet_data_source.init_app(app)
