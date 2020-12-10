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

import bson
import marshmallow as ma
from marshmallow import validate, ValidationError, missing

CHART_PARAMETERS_AXIS = ['X', 'Y', 'Z', 'T', 'P', 'S']


class ObjectId(ma.fields.Field):
    def _deserialize(self, value, attr, data, **kwargs):
        try:
            return bson.ObjectId(value)
        except Exception:
            raise ValidationError("invalid ObjectId `%s`" % value)

    def _serialize(self, value, attr, obj, **kwargs):
        if value is None:
            return missing
        return str(value)


def axis_field(required: bool = False):
    return ma.fields.String(validate=validate.OneOf(CHART_PARAMETERS_AXIS), required=required)


def aggregation_parameter_type_field(required: bool = False):
    return ma.fields.String(validate=validate.OneOf(['A', 'C']), required=required)


def analytic_type_field(required: bool = False):
    return ma.fields.String(validate=validate.OneOf(['CHART', 'TABLE']), required=required)


def chart_options(required: bool = False):
    return ma.fields.String(validate=validate.OneOf(['SCATTER', 'BARCHART', 'PIECHART']), required=required)


def grid_break_points(required: bool = False):
    return ma.fields.String(validate=validate.OneOf(['lg', 'md', 'sm', 'xs', 'xxs']), required=required)


def grid_position(required: bool = False):
    return ma.fields.Dict(
        ma.fields.String(
            validate=validate.OneOf(['x', 'y', 'w', 'h', 'i', 'minH', 'minW', 'maxH', 'maxW', 'moved', 'static'])),
        required=required)


class DateStringField(ma.fields.String):
    default_error_messages = {"invalid": "Not a valid date must be YYYY-MM-DD"}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Insert validation into self.validators so that multiple errors can be stored.
        validator = validate.Regexp(
            regex=r'(?P<year>\d{4})-(?P<month>\d{1,2})-(?P<day>\d{1,2})$',
            error=self.error_messages["invalid"],
        )
        self.validators.insert(0, validator)


class NonEmptyString(ma.fields.String):
    default_error_messages = {"invalid": "must not be empty"}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        validator = validate.Length(min=1, error=self.error_messages["invalid"])
        self.validators.insert(0, validator)


class Filter(ma.Schema):
    filterId = NonEmptyString(required=True)
    value = ma.fields.String()
    valid = ma.fields.Boolean()

    class Meta:
        unknown = ma.EXCLUDE


class AggregationParameter(ma.Schema):
    parameterId = NonEmptyString(required=True)
    label = NonEmptyString(required=True)
    valid = ma.fields.Boolean()
    type = aggregation_parameter_type_field()
    value = NonEmptyString()
    top = ma.fields.Integer()

    class Meta:
        unknown = ma.EXCLUDE


class ChartAggregationParameter(AggregationParameter):
    axis = axis_field()

    class Meta:
        unknown = ma.EXCLUDE


class Chart(ma.Schema):
    type = chart_options()
    title = ma.fields.String()
    legend = ma.fields.String()
    description = ma.fields.String()
    axis = ma.fields.Mapping(axis_field(), ma.fields.String(), required=True)
    parameters = ma.fields.List(ma.fields.Nested(ChartAggregationParameter), required=True)

    class Meta:
        unknown = ma.EXCLUDE


class TableAggregationParameter(AggregationParameter):
    class Meta:
        unknown = ma.EXCLUDE


class Table(ma.Schema):
    title = ma.fields.String()
    legend = ma.fields.String()
    description = ma.fields.String()
    parameters = ma.fields.List(ma.fields.Nested(TableAggregationParameter), required=True)

    class Meta:
        unknown = ma.EXCLUDE


class AnalyticArgSchema(ma.Schema):
    type = analytic_type_field()
    chart = ma.fields.Nested(Chart)
    table = ma.fields.Nested(Table)
    filter = ma.fields.Nested(Filter)

    class Meta:
        unknown = ma.EXCLUDE


class AnalyticSchema(ma.Schema):
    analyticId = NonEmptyString(required=True)
    type = analytic_type_field()
    chart = ma.fields.Nested(Chart)
    table = ma.fields.Nested(Table)
    filter = ma.fields.Nested(Filter)
    version = ma.fields.String()

    class Meta:
        unknown = ma.EXCLUDE


class Column(ma.Schema):
    columnId = NonEmptyString(required=True)

    class Meta:
        unknown = ma.EXCLUDE


class DataSource(ma.Schema):
    sourceId = NonEmptyString(required=True)

    class Meta:
        unknown = ma.EXCLUDE


class DataSourceColumns(DataSource):
    columns = ma.fields.List(ma.fields.Nested(Column), required=True)

    class Meta:
        unknown = ma.EXCLUDE


class JoinTable(ma.Schema):
    joinSourceId = NonEmptyString(required=True)
    onLeft = ma.fields.List(ma.fields.Nested(Column), required=True)
    onRight = ma.fields.List(ma.fields.Nested(Column), required=True)
    defaultValues = ma.fields.Mapping(ma.fields.String(required=True), required=True)

    class Meta:
        unknown = ma.EXCLUDE


class ScopeSchema(ma.Schema):
    scopeId = NonEmptyString(required=True)

    filter = ma.fields.Nested(Filter)
    source = ma.fields.Nested(DataSource)
    columns = ma.fields.List(ma.fields.Nested(Column), required=True)
    joins = ma.fields.List(ma.fields.Nested(JoinTable), required=True)

    class Meta:
        unknown = ma.EXCLUDE


class ScopeOptionsSchema(ScopeSchema):
    sources = ma.fields.List(ma.fields.Nested(DataSource), required=True)
    sourceColumns = ma.fields.List(ma.fields.Nested(DataSourceColumns), required=True)
    filters = ma.fields.List(ma.fields.Nested(Column), required=True)
    categories = ma.fields.List(ma.fields.Nested(Column), required=True)
    measures = ma.fields.List(ma.fields.Nested(Column), required=True)

    class Meta:
        unknown = ma.EXCLUDE


class GridSchema(ma.Schema):
    layouts = ma.fields.Dict(grid_break_points(), ma.fields.List(grid_position()), required=True)

    class Meta:
        unknown = ma.EXCLUDE


class ChartSettings(ma.Schema):
    typeOptions = ma.fields.Dict(chart_options(),
                                 ma.fields.String(), required=True)

    class Meta:
        unknown = ma.EXCLUDE


class GridSettings(ma.Schema):
    width = ma.fields.Number(default=1200)
    rowHeight = ma.fields.Number(default=30)
    cols = ma.fields.Mapping(grid_break_points(), ma.fields.Number(), required=True)
    breakPoints = ma.fields.Mapping(grid_break_points(), ma.fields.Number(), required=True)

    class Meta:
        unknown = ma.EXCLUDE


class SettingsSchema(ma.Schema):
    chart = ma.fields.Nested(ChartSettings)
    grid = ma.fields.Nested(GridSettings)

    class Meta:
        unknown = ma.EXCLUDE


class DashboardDescription(ma.Schema):
    _id = ObjectId(data_key='dashboardId')
    dashboardTitle = NonEmptyString(required=True)
    dashboardDescription = ma.fields.String()
    createdBy = NonEmptyString()
    version = ma.fields.Number()
    settings = ma.fields.Nested(SettingsSchema)

    class Meta:
        unknown = ma.EXCLUDE


class DashboardSchema(DashboardDescription):
    analytics = ma.fields.List(ma.fields.Nested(AnalyticSchema), required=True)
    scope = ma.fields.Nested(ScopeSchema)
    grid = ma.fields.Nested(GridSchema)

    class Meta:
        unknown = ma.EXCLUDE


class EmbedArgSchema(ma.Schema):
    type = analytic_type_field()
    minSizeX = ma.fields.Number()
    minSizeY = ma.fields.Number()
    maxSizeX = ma.fields.Number()
    maxSizeY = ma.fields.Number()

    class Meta:
        unknown = ma.EXCLUDE


class EmbedSchema(ma.Schema):
    srcPath = NonEmptyString()
    appPath = NonEmptyString()
    elementId = NonEmptyString()
    analyticId = NonEmptyString()
    headers = ma.fields.Mapping(ma.fields.String(required=True), ma.fields.String(), required=True)

    class Meta:
        unknown = ma.EXCLUDE


class AggregateQuerySchema(ma.Schema):
    source = ma.fields.Nested(DataSource, required=True)
    filters = ma.fields.List(NonEmptyString(), required=True)
    aggregates = ma.fields.Mapping(ma.fields.String(required=True), NonEmptyString(), required=True)
    dimensions = ma.fields.List(NonEmptyString(), required=True)

    class Meta:
        unknown = ma.EXCLUDE


class AggregateSplitSchema(ma.Schema):
    columns = ma.fields.List(ma.fields.Raw(), required=True)
    index = ma.fields.List(ma.fields.Raw(), required=True)
    data = ma.fields.List(ma.fields.Raw(), required=True)


def is_valid_filter(filter_spec):
    return filter_spec and filter_spec['value'] and len(filter_spec['value']) > 0 and filter_spec['valid']


def is_valid_aggregate(aggregate_spec):
    return aggregate_spec and aggregate_spec['type'] == 'A' and aggregate_spec['value'] and len(
        aggregate_spec['value']) > 0 and aggregate_spec['valid']


def is_valid_dimension(aggregate_spec):
    return aggregate_spec and aggregate_spec['type'] == 'C' and aggregate_spec['value'] and len(
        aggregate_spec['value']) > 0


def is_chart(analytic_spec):
    return analytic_spec.get('type', None) and analytic_spec.get('type', None) == 'CHART'


def is_table(analytic_spec):
    return analytic_spec.get('type', None) and analytic_spec.get('type', None) == 'TABLE'
