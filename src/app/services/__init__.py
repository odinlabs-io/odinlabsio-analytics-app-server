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

from app.db import parquet_data_source, mongo_data_source
from app.services.analytic_service import AnalyticsService
from app.services.bokeh_service import BokehService
from app.services.dashboard_service import DashboardService
from app.services.plot_service import PlotService

analytics_service = AnalyticsService()
dashboard_service = DashboardService()
plot_service = PlotService()
bokeh_service = BokehService()


def init_app(app: Flask):
    bokeh_service.init_app(app)
    analytics_service.init_app(parquet_data_source=parquet_data_source)
    dashboard_service.init_app(mongo_data_source=mongo_data_source, parquet_data_source=parquet_data_source)
    plot_service.init_app(analytics_service=analytics_service, dashboard_service=dashboard_service)
