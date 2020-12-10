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

import json

import flask.views
import flask_smorest

from app.model import AggregateQuerySchema, AggregateSplitSchema


class AggregateAPI:
    def init_app(self, app, api, analytics_service):
        aggregate_api = flask_smorest.Blueprint('aggregate', 'aggregate', url_prefix='/api/aggregate',
                                                description='Aggregate API')

        @aggregate_api.route('')
        class Aggregate(flask.views.MethodView):

            @aggregate_api.arguments(AggregateQuerySchema(), location='json')
            @aggregate_api.response(AggregateSplitSchema())
            def post(self, data):
                data_set_name = data['source']['sourceId']
                filters = data['filters']
                aggregates = [(aggr_name, aggr_value) for aggr_name, aggr_value in data['aggregates'].items()]
                dimensions = [(dim_name, dim_name) for dim_name in data['dimensions']]

                df = analytics_service.get_aggregate(data_set=data_set_name, filters=filters,
                                                     aggregates=aggregates, dimensions=dimensions)

                return json.loads(df.to_json(orient="split"))

        api.register_blueprint(aggregate_api)
