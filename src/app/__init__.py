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
from typing import Dict, Any

from bokeh.document import Document
from flask import Flask
from flask_cors import CORS
from flask_smorest import Api

from app import db, services, apis, controller
from app.services import plot_service


def flask_app(local: Dict[str, Any]):
    api = Api()
    app = Flask('app')
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    if local:
        app.config.update(local)
    # load default properties
    app.config.from_object(os.environ.get('APP_CONF'))
    # load env properties
    if 'ENV_CONF' in os.environ:
        app.config.from_envvar('ENV_CONF')

    app.template_folder = app.config['TEMPLATE_FOLDER']
    app.static_folder = app.config['STATIC_FOLDER']
    app.static_url_path = app.config['STATIC_URL_PATH']

    # init data source
    db.init_app(app)
    # init services
    services.init_app(app)

    # register api and init app apis
    api.init_app(app)
    apis.init_app(app, api)

    # init server controller
    controller.init_app(app)

    print(app.url_map)

    return app


def bk_app():
    def bokeh_app(doc: Document):
        arguments = doc.session_context.request.arguments

        dashboard_id = str(arguments.get('dashboardId')[0], 'utf-8')
        analytic_id = str(arguments.get('analyticId')[0], 'utf-8')

        plot = plot_service.plot(dashboard_id=dashboard_id, analytic_id=analytic_id)
        if plot:
            doc.add_root(plot)

        # doc.theme = Theme(filename=app.config.get('TEMPLATE_FOLDER') + "theme.yaml")

    return bokeh_app
