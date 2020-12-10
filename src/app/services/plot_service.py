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

import itertools
from collections import defaultdict
from math import pi
from typing import Dict

from bokeh.layouts import column
from bokeh.models import ColumnDataSource, FactorRange, Range1d, LinearAxis, PreText
from bokeh.palettes import Spectral11
from bokeh.plotting import figure
from bokeh.transform import cumsum

from app.model import is_valid_aggregate, is_valid_dimension
from app.model.model import CHART_PARAMETERS_AXIS, is_valid_filter

TOOLS = "hover,crosshair,pan,wheel_zoom,zoom_in,zoom_out,box_zoom,undo,redo,reset,tap,save,box_select,poly_select,lasso_select,"

PALETTE = Spectral11

ALPHA = 0.8


class PlotService:
    def __init__(self):
        self._analytics_service = None
        self._dashboard_service = None
        self._axis_order = defaultdict(lambda: 0, {})

    def init_app(self, analytics_service, dashboard_service):
        self._analytics_service = analytics_service
        self._dashboard_service = dashboard_service
        self._axis_order = defaultdict(lambda: len(CHART_PARAMETERS_AXIS),
                                       {axe: i for i, axe in enumerate(CHART_PARAMETERS_AXIS, 0)})

    def _axis_index(self, axis, sort_by):
        axis_order = self._axis_order

        axis = sorted([(axe, axis_order[axe[sort_by]]) for axe in axis], key=lambda x: x[1])

        return [axe[0] for axe in axis]

    def _generate_value_tooltips(self, fields, fields_legend):
        return [(legend, "@" + field) for field, legend in zip(fields, fields_legend)]

    def _color(self, values):

        return self._color_def(values, color_dict=dict())

    def _color_def(self, values, color_dict):
        color_palette = itertools.cycle(PALETTE)
        colors = []
        for c in values:
            color = color_dict.get(c)
            if not color:
                color_dict[c] = next(color_palette)
            colors.append(color_dict[c])

        return colors

    def _bar_chart(self, labels: Dict[str, str], df):
        dimensions = df.index.names
        aggregates = df.columns

        if len(dimensions) == 1:
            aggr_0 = aggregates[0]

            # normal vbar and line for other aggregates
            factors = [factor for factor in df.index.values]
            data = dict({'x': factors, 'aggr_0': [v for v in df[aggr_0].values]})
            data['color'] = self._color(factors)

            tooltips_var = []
            tooltips_label = []
            extra_y_ranges = {}
            if len(aggregates) > 1:

                for i in range(1, len(aggregates)):
                    aggr_n = aggregates[i]
                    aggr_n_name = 'aggr_' + str(i)
                    tooltips_var.append(aggr_n)
                    tooltips_label.append(aggr_n_name)
                    data[aggr_n_name] = df[aggr_n]
                    extra_y_ranges[aggr_n_name] = Range1d(start=df[aggr_n].min() - 10, end=df[aggr_n].max() + 10)

            p = figure(x_range=factors, tools=TOOLS,
                       tooltips=[('Value', "@x: @aggr_0")] + self._generate_value_tooltips(tooltips_label,
                                                                                           tooltips_var))

            source = ColumnDataSource(data=data)
            p.vbar(x='x', top='aggr_0', source=source, width=0.9, alpha=ALPHA, legend_field='x',
                   fill_color='color')

            if len(aggregates) > 1:
                color_palette = itertools.cycle(PALETTE)
                p.extra_y_ranges = extra_y_ranges
                for i in range(1, len(aggregates)):
                    aggr_n = aggregates[i]
                    aggr_n_name = 'aggr_' + str(i)
                    color = next(color_palette)

                    p.line(x='x', y=aggr_n_name, color=color, y_range_name=aggr_n_name,
                           source=source)
                    p.add_layout(LinearAxis(y_range_name=aggr_n_name, axis_label=aggr_n), 'left')
                    p.yaxis[i].major_label_text_color = color

            p.yaxis[0].axis_label = aggr_0
            p.legend.title = labels.get(dimensions[0], dimensions[0])
            p.add_layout(p.legend[0], 'right')

            p.xaxis.major_label_orientation = 1
            p.xgrid.grid_line_color = None
            return p
        elif len(dimensions) == 2:
            # stacked bar chart
            aggr_0 = aggregates[0]

            unstacked = df.unstack(-1)

            factors = [factor for factor in unstacked.index]
            data = dict({'x': factors})
            aggr_column = unstacked[aggr_0]
            unstacked_values = [v for v in aggr_column.columns]
            color = []
            colors = itertools.cycle(PALETTE)
            for memb in unstacked_values:
                data[memb] = [v for v in aggr_column[memb].fillna(0).values]
                color.append(next(colors))

            p = figure(x_range=factors, tools=TOOLS, tooltips="$name @x: @$name")

            source = ColumnDataSource(data=data)
            p.vbar_stack(unstacked_values, x='x', source=source, color=color, width=0.9, alpha=ALPHA,
                         legend_label=unstacked_values)

            p.legend.title = labels.get(dimensions[-1], dimensions[-1])
            p.add_layout(p.legend[0], 'right')

            p.yaxis.axis_label = aggr_0

            p.xaxis.major_label_orientation = 1
            p.xgrid.grid_line_color = None
            return p
        elif len(dimensions) == 3 or len(dimensions) == 4:
            # group by n-1 first and stack by last dimension
            aggr_0 = aggregates[0]

            unstacked = df.unstack(-1)
            factors = [factor for factor in unstacked.index]
            data = dict({'x': factors})
            aggr_column = unstacked[aggr_0]
            unstacked_values = [v for v in aggr_column.columns]
            color = []
            colors = itertools.cycle(PALETTE)
            for memb in unstacked_values:
                data[memb] = [v for v in aggr_column[memb].fillna(0).values]
                color.append(next(colors))

            source = ColumnDataSource(data=data)
            p = figure(x_range=FactorRange(*factors), tools=TOOLS, tooltips="$name @x: @$name")
            p.vbar_stack(unstacked_values, x='x', source=source, color=color, width=0.9, alpha=ALPHA,
                         legend_label=unstacked_values)

            p.legend.title = labels.get(dimensions[-1], dimensions[-1])
            p.add_layout(p.legend[0], 'right')

            p.yaxis.axis_label = aggr_0

            p.xaxis.major_label_orientation = 1
            p.xgrid.grid_line_color = None
            return p
        else:
            p = PreText(text="""Bar Chart accepts 1 to 4 dimensions.""", width=500, height=100)

            return p

    def _pie_chart(self, labels: Dict[str, str], df):
        dimensions = df.index.names
        aggregates = df.columns
        if len(dimensions) == 1 and len(aggregates) != 0:
            aggr_0 = aggregates[0]
            category = dimensions[0]

            data = dict()
            df = df.reset_index()

            aggr_0_sum = df[aggr_0].sum()

            data['value'] = df[aggr_0]
            data['angle'] = df[aggr_0] / aggr_0_sum * 2 * pi
            data['percentage'] = df[aggr_0] / aggr_0_sum * 100
            data['color'] = self._color(df[category])
            data['category'] = df[category]
            data['legend'] = [l + ": {:.2f} %".format(v) for l, v in zip(data['category'], data['percentage'])]

            source = ColumnDataSource(data=data)
            p = figure(tools=TOOLS, tooltips="@category:@value / @percentage")
            p.wedge(x=0, y=0, radius=0.8, start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
                    line_color="white", fill_color='color', legend_field='legend', source=source)

            p.legend.title = labels.get(category, category)
            p.add_layout(p.legend[0], 'right')

            p.xaxis.major_label_orientation = 1
            p.xgrid.grid_line_color = None
            p.toolbar.autohide = True
            return p
        else:
            p = PreText(text="""Pie chart accepts at most one aggregate and a dimension.""", width=500, height=100)

            return p

    def _scatter_chart(self, labels: Dict[str, str], df):
        dimensions = df.index.names
        aggregates = df.columns
        if len(aggregates) == 1:
            aggr_0 = aggregates[0]

            if len(dimensions) == 1:
                factors = [factor for factor in df.index]
                p = figure(x_range=factors, tools=TOOLS, tooltips="@x: @aggr_0")

                category = dimensions[0]
                data = dict({'x': factors, 'aggr_0': [v for v in df[aggr_0].values]})
                p.line(x='x', y='aggr_0', source=ColumnDataSource(data=data))
                p.xaxis.axis_label = labels.get(category, category)
                p.yaxis.axis_label = aggr_0

                p.xaxis.major_label_orientation = 1
                p.xgrid.grid_line_color = None
                p.toolbar.autohide = True

                return p
            elif len(dimensions) == 2 or len(dimensions) == 3 or len(dimensions) == 4:
                # unstack first
                unstacked = df.stack().unstack(-2).unstack(-1)

                p = figure(x_range=FactorRange(*unstacked.index), tools=TOOLS,
                           tooltips=self._generate_value_tooltips(['x', 'aggr_0', 'category'],
                                                                  ["", aggr_0, labels.get(dimensions[-1])]))
                color_dict = dict()
                stacked_columns = list(set([i[0] for i in unstacked.columns]))
                self._color_def(stacked_columns, color_dict=color_dict)
                aggr_0_values = []
                factors = []
                categories = []
                for cat in stacked_columns:
                    cat_column = unstacked[cat].dropna()
                    aggr_0_values += cat_column[aggr_0].values.tolist()
                    factors += [i for i in cat_column.index]
                    categories += [cat for i in range(len(cat_column))]

                colors = [color_dict[cat_val] for cat_val in categories]

                data = dict({'x': factors, 'aggr_0': aggr_0_values, 'category': categories,
                             'color': colors})

                p.scatter(x='x', y='aggr_0', size=10,
                          fill_color='color',
                          fill_alpha=ALPHA,
                          source=ColumnDataSource(data),
                          legend_group='category')

                p.legend.title = labels.get(dimensions[-1], dimensions[-1])
                p.add_layout(p.legend[0], 'right')
                p.yaxis.axis_label = aggr_0
                p.xaxis.axis_label = "/".join([labels.get(dim, dim) for dim in dimensions[:-1]])

                p.xaxis.major_label_orientation = 1
                p.xgrid.grid_line_color = None
                p.toolbar.autohide = True

                return p
            else:
                p = PreText(text="""Scatter Plot 1 aggregates accepts at most 4 dimensions.""", width=500, height=100)

                return p
        elif len(aggregates) == 2:
            aggr_0 = aggregates[0]
            aggr_1 = aggregates[1]

            if len(dimensions) == 1:
                df = df.reset_index()
                category = dimensions[0]

                data = dict()
                data['aggr_0'] = df[aggr_0]
                data['aggr_1'] = df[aggr_1]

                data['category'] = df[category]
                data['color'] = self._color(df[category])

                p = figure(tools=TOOLS, tooltips=self._generate_value_tooltips(['aggr_0', 'aggr_1', 'category'],
                                                                               [aggr_0, aggr_1,
                                                                                labels.get(category, category)]))
                p.scatter(x='aggr_0', y='aggr_1',
                          source=ColumnDataSource(data=data),
                          fill_color='color',
                          fill_alpha=ALPHA,
                          legend_group='category')

                p.legend.title = labels.get(category, category)
                p.add_layout(p.legend[0], 'right')
                p.xaxis.axis_label = aggr_0
                p.yaxis.axis_label = aggr_1
                p.add_layout(p.legend[0], 'right')

                p.xaxis.major_label_orientation = 1
                p.xgrid.grid_line_color = None
                p.toolbar.autohide = True

                return p
            elif len(dimensions) == 2 or len(dimensions) == 3 or len(dimensions) == 4:
                unstacked = df.stack().unstack(-2).unstack(-1)

                p = figure(x_range=FactorRange(*unstacked.index), tools=TOOLS,
                           tooltips=self._generate_value_tooltips(['x', 'aggr_0', 'aggr_1', 'category'],
                                                                  ["", aggr_0, aggr_1, labels.get(dimensions[-1])]))
                color_dict = dict()
                stacked_columns = list(set([i[0] for i in unstacked.columns]))
                self._color_def(stacked_columns, color_dict=color_dict)
                aggr_0_values = []
                aggr_1_values = []
                factors = []
                categories = []
                for cat in stacked_columns:
                    cat_column = unstacked[cat].dropna()
                    aggr_0_values += cat_column[aggr_0].values.tolist()
                    aggr_1_values += cat_column[aggr_1].values.tolist()
                    factors += [i for i in cat_column.index]
                    categories += [cat for i in range(len(cat_column))]

                colors = [color_dict[cat_val] for cat_val in categories]

                data = dict({'x': factors, 'aggr_0': aggr_0_values, 'aggr_1': aggr_1_values, 'category': categories,
                             'color': colors})

                p.scatter(x='x', y='aggr_0', size='aggr_1',
                          fill_color='color',
                          fill_alpha=ALPHA,
                          source=ColumnDataSource(data),
                          legend_group='category')

                p.legend.title = labels.get(dimensions[-1], dimensions[-1])
                p.add_layout(p.legend[0], 'right')
                p.yaxis.axis_label = aggr_0
                p.xaxis.axis_label = "/".join([labels.get(dim, dim) for dim in dimensions[:-1]])

                p.xaxis.major_label_orientation = 1
                p.xgrid.grid_line_color = None
                p.toolbar.autohide = True

                return p
            else:
                # get first dimension (more than one dimension => duplicates in plot)
                df = df.reset_index()
                category = dimensions[0]

                data = dict()
                data['aggr_0'] = df[aggr_0]
                data['aggr_1'] = df[aggr_1]

                data['category'] = df[category]
                data['color'] = self._color(df[category])

                p = figure(tools=TOOLS,
                           tooltips=self._generate_value_tooltips(['aggr_0', 'aggr_1', 'category'],
                                                                  [aggr_0, aggr_1, labels.get(category, category)]))
                p.scatter(x='aggr_0', y='aggr_1',
                          source=ColumnDataSource(data=data),
                          fill_color='color',
                          fill_alpha=ALPHA, legend_group='category')

                p.legend.title = labels.get(category, category)
                p.xaxis.axis_label = aggr_0
                p.yaxis.axis_label = aggr_1
                p.add_layout(p.legend[0], 'right')

                p.xaxis.major_label_orientation = 1
                p.xgrid.grid_line_color = None
                p.toolbar.autohide = True

                return p
        else:
            # get first dimension (more than one dimension => duplicates in plot)
            df = df.reset_index()
            aggr_0 = aggregates[0]
            aggr_1 = aggregates[1]
            aggr_2 = aggregates[2]
            category = dimensions[0]

            data = dict()
            data['aggr_0'] = df[aggr_0]
            data['aggr_1'] = df[aggr_1]
            data['aggr_2'] = df[aggr_2]

            data['category'] = df[category]
            data['color'] = self._color(df[category])

            p = figure(tools=TOOLS, tooltips=self._generate_value_tooltips(['aggr_0', 'aggr_1', 'aggr_2', 'category'],
                                                                           [aggr_0, aggr_1, aggr_2,
                                                                            labels.get(category, category)]))
            p.scatter(x='aggr_0', y='aggr_1', size='aggr_2',
                      source=ColumnDataSource(data=data),
                      fill_color='color',
                      fill_alpha=ALPHA, legend_group='category')

            p.legend.title = labels.get(category, category)
            p.xaxis.axis_label = aggr_0
            p.yaxis.axis_label = aggr_1
            p.add_layout(p.legend[0], 'right')

            p.xaxis.major_label_orientation = 1
            p.xgrid.grid_line_color = None
            p.toolbar.autohide = True

            return p

    def plot(self, dashboard_id: str, analytic_id: str):

        if not dashboard_id or not analytic_id:
            return

        scope = self._dashboard_service.get_scope(dashboard_id=dashboard_id)
        analytic = self._dashboard_service.get_analytic(dashboard_id=dashboard_id, analytic_id=analytic_id)

        if scope and analytic and scope['source']:
            widget_type = analytic.get('type', None)

            if widget_type == 'CHART':
                chart_type = analytic['chart']['type']
                parameters = analytic['chart']['parameters']
                axis = []
                # build tuple (type, label, value (expression or dim name), chart axis, topk, column in df (aggreg label or dimension name)
                for parameter in parameters:
                    if is_valid_aggregate(parameter):
                        axis.append(('A', parameter['label'], parameter['value'], parameter.get('axis', None),
                                     parameter.get('top', None), parameter['label']))
                    elif is_valid_dimension(parameter):
                        axis.append(('C', parameter['label'], parameter['value'], parameter.get('axis', None),
                                     parameter.get('top', None), parameter['value']))

                # sort axis
                ordered_axis = self._axis_index(axis, sort_by=3)
                aggregates = [(axe[1], axe[2]) for axe in ordered_axis if axe[0] == 'A']
                dimensions = [(axe[1], axe[2]) for axe in ordered_axis if axe[0] == 'C']
                data_set_name = scope['source']['sourceId']
                # filters
                filters = []
                scope_filter = scope.get('filter', None)
                if is_valid_filter(scope_filter):
                    filters.append(scope_filter['value'])
                analytic_filter = analytic.get('filter', None)
                if is_valid_filter(analytic_filter):
                    filters.append(analytic_filter['value'])

                df = self._analytics_service.get_aggregate(data_set=data_set_name, filters=filters,
                                                           aggregates=aggregates, dimensions=dimensions)

                topk = [(axe[1], axe[4]) for axe in ordered_axis if axe[0] == 'A']
                for top_name, top_value in topk:
                    if top_value:
                        df = df.nlargest(top_value, columns=[top_name])

                labels = {axe[5]: axe[1] for axe in ordered_axis}

                if chart_type == 'BARCHART':
                    plot = self._bar_chart(labels, df)
                elif chart_type == 'PIECHART':
                    plot = self._pie_chart(labels, df)
                else:
                    plot = self._scatter_chart(labels, df)

                return column(plot)
