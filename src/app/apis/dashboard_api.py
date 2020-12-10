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
import uuid

import flask.views
import flask_smorest
import shortuuid
from webargs.flaskparser import abort

from app.model import DashboardSchema, AnalyticSchema, ScopeSchema, GridSchema, EmbedSchema, \
    EmbedArgSchema, SettingsSchema
from app.model.model import DashboardDescription, ScopeOptionsSchema


class DashboardAPI:

    def init_app(self, app, api, dashboard_service, bokeh_service):
        dashboard_api = flask_smorest.Blueprint('dashboard', 'dashboard', url_prefix='/api/dashboard',
                                                description='Dashboard API')
        with open(app.config.get('DEFAULT_DASHBOARD_TEMPLATE_PATH')) as json_file:
            default_json = json.load(json_file)

        @dashboard_api.route('')
        class Dashboard(flask.views.MethodView):

            @dashboard_api.arguments(DashboardDescription(), location='json')
            @dashboard_api.response(DashboardSchema())
            def post(self, data):
                dashboard_id = str(uuid.uuid4().hex)
                settings = data.get('settings')
                if not settings:
                    data['settings'] = default_json['settings']
                grid = data.get('grid')
                if not grid:
                    data['grid'] = default_json['grid']
                analytics = data.get('analytics')
                if not analytics:
                    data['analytics'] = []

                return dashboard_service.save_dashboard(dashboard_id=dashboard_id, dashboard=data)

            @dashboard_api.response(DashboardDescription(many=True))
            def get(self):
                return dashboard_service.get_dashboards()

        @dashboard_api.route('/<string:dashboard_id>')
        class DashboardById(flask.views.MethodView):

            @dashboard_api.response(DashboardSchema())
            def get(self, dashboard_id):
                return dashboard_service.get_dashboard(dashboard_id=dashboard_id)

            @dashboard_api.arguments(DashboardSchema(), location='json')
            @dashboard_api.response(DashboardSchema())
            def put(self, data, dashboard_id):
                return dashboard_service.save_dashboard(dashboard_id=dashboard_id, dashboard=data)

        @dashboard_api.route('/<string:dashboard_id>/analytics')
        class AnalyticsCollection(flask.views.MethodView):

            @dashboard_api.response(AnalyticSchema(many=True))
            def get(self, dashboard_id):
                return dashboard_service.get_analytics(dashboard_id=dashboard_id)

            @dashboard_api.response(AnalyticSchema())
            def post(self, dashboard_id):
                analytic_id = shortuuid.uuid()

                return dashboard_service.add_analytic(dashboard_id=dashboard_id, analytic_id=analytic_id, analytic={})

        @dashboard_api.route('/<string:dashboard_id>/analytics/<string:analytic_id>')
        class AnalyticById(flask.views.MethodView):

            @dashboard_api.response(AnalyticSchema())
            def get(self, analytic_id, dashboard_id):
                return dashboard_service.get_analytic(dashboard_id=dashboard_id, analytic_id=analytic_id)

            @dashboard_api.arguments(AnalyticSchema(), location='json')
            @dashboard_api.response(AnalyticSchema())
            def put(self, data, analytic_id, dashboard_id):
                return dashboard_service.add_analytic(dashboard_id=dashboard_id, analytic_id=analytic_id, analytic=data)

            @dashboard_api.response(code=204)
            def delete(self, analytic_id, dashboard_id):
                if not dashboard_service.remove_analytic(dashboard_id=dashboard_id, analytic_id=analytic_id):
                    abort(404, "Analytic does not exist")

        @dashboard_api.route('/<string:dashboard_id>/analytics/<string:analytic_id>/embed')
        class Embed(flask.views.MethodView):

            @dashboard_api.arguments(EmbedArgSchema(), location='query')
            @dashboard_api.response(EmbedSchema())
            def get(self, arg, analytic_id, dashboard_id):
                analytic = dashboard_service.get_analytic(dashboard_id=dashboard_id, analytic_id=analytic_id)

                if not analytic:
                    abort(404, 'Analytic {} not found'.format(analytic_id))
                else:
                    return bokeh_service.get_server_session(dashboard_id=dashboard_id,
                                                            analytic_id=analytic_id,
                                                            args=arg)

        @dashboard_api.route('/<string:dashboard_id>/scope')
        class Scope(flask.views.MethodView):

            @dashboard_api.response(ScopeOptionsSchema())
            def get(self, dashboard_id):
                return dashboard_service.get_scope(dashboard_id=dashboard_id)

            @dashboard_api.arguments(ScopeSchema(), location='json')
            @dashboard_api.response(ScopeOptionsSchema())
            def put(self, data, dashboard_id):
                return dashboard_service.update_scope(dashboard_id=dashboard_id, scope=data)

        @dashboard_api.route('/<string:dashboard_id>/grid')
        class Grid(flask.views.MethodView):

            @dashboard_api.response(GridSchema())
            def get(self, dashboard_id):
                return dashboard_service.get_grid(dashboard_id=dashboard_id)

            @dashboard_api.arguments(GridSchema(), location='json')
            @dashboard_api.response(GridSchema())
            def put(self, data, dashboard_id):
                return dashboard_service.update_grid(dashboard_id=dashboard_id, grid=data)

        @dashboard_api.route('/<string:dashboard_id>/settings')
        class Settings(flask.views.MethodView):

            @dashboard_api.response(SettingsSchema())
            def get(self, dashboard_id):
                return dashboard_service.get_settings(dashboard_id=dashboard_id)

        api.register_blueprint(dashboard_api)
