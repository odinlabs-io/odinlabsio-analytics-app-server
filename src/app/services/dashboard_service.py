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

from typing import Any

import pymongo
import shortuuid

from app.db import MongoDataSource, ParquetDataSource

DASHBOARD_COLLECTION = 'dashboard'
"""
DASHBOARD SERVICE
"""


class DashboardService():
    def __init__(self):
        self._mongo_data_source: MongoDataSource = None
        self._parquet_data_source: ParquetDataSource = None

    def init_app(self, mongo_data_source: MongoDataSource, parquet_data_source: ParquetDataSource):
        self._mongo_data_source = mongo_data_source
        self._parquet_data_source = parquet_data_source

    def get_dashboards(self):
        return [dashboard for dashboard in self._mongo_data_source.get_db()[DASHBOARD_COLLECTION].find({}, {
            'dashboardTitle': 1, 'dashboardDescription': 1, 'createdBy': 1, 'version': 1
        })]

    def get_dashboard(self, dashboard_id: str):
        return self._mongo_data_source.get_db()[DASHBOARD_COLLECTION].find_one(
            {
                '_id': dashboard_id
            })

    def save_dashboard(self, dashboard_id: str, dashboard: Any):
        updates = []
        for k, v in dashboard.items():
            updates.append(
                {
                    '$set':
                        {
                            k: v
                        }
                })

        return self._mongo_data_source.get_db()[DASHBOARD_COLLECTION].find_one_and_update(
            {
                '_id': dashboard_id
            }, updates, upsert=True, return_document=pymongo.ReturnDocument.AFTER)

    def get_analytics(self, dashboard_id):
        _dashboard = self._mongo_data_source.get_db()[DASHBOARD_COLLECTION].find_one(
            {
                '_id': dashboard_id
            })

        if _dashboard:
            return _dashboard['analytics']
        else:
            return []

    def get_analytic(self, dashboard_id: str, analytic_id: str):
        result = self._mongo_data_source.get_db()[DASHBOARD_COLLECTION].find_one(
            {
                '_id': dashboard_id,
                'analytics':
                    {
                        '$elemMatch': {'analyticId': analytic_id}
                    }
            }, {
                'analytics.$': 1
            })

        if result:

            return result['analytics'][0]
        else:

            return {}

    def add_analytic(self, dashboard_id, analytic_id: str, analytic: Any):
        dashboards = self._mongo_data_source.get_db()[DASHBOARD_COLLECTION]

        _analytic = dict(analytic)
        _analytic['analyticId'] = analytic_id
        _analytic['version'] = shortuuid.uuid()

        updated = dashboards.update_one(
            {
                '_id': dashboard_id,
                'analytics.analyticId':
                    {
                        '$ne': analytic_id
                    }
            },
            {
                '$push':
                    {
                        'analytics': _analytic
                    }
            })

        if updated.matched_count == 0:
            updated = dashboards.update_one(
                {
                    '_id': dashboard_id,
                    'analytics.analyticId': analytic_id
                },
                {
                    '$set':
                        {
                            'analytics.$': _analytic
                        }
                })

            if updated.matched_count != 0:
                return _analytic
            else:
                return {}
        else:
            return _analytic

    def remove_analytic(self, dashboard_id: str, analytic_id: str):
        removed = self._mongo_data_source.get_db()[DASHBOARD_COLLECTION].update_one(
            {
                '_id': dashboard_id
            },
            {
                '$pull': {'analytics': {'analyticId': analytic_id}}
            }
        )

        if removed.matched_count != 0:
            return True
        else:
            return False

    def _get_column_ids(self, source_name):
        return [{'columnId': field['name']} for field in self._parquet_data_source.get_columns(source_name)]

    def _get_category_ids(self, source_name):
        return [{'columnId': field['name']} for field in self._parquet_data_source.get_categories(source_name)]

    def _get_measure_ids(self, source_name):
        return [{'columnId': field['name']} for field in self._parquet_data_source.get_measures(source_name)]

    def _get_empty_scope(self):
        source_names = self._parquet_data_source.get_sources()
        categories, measures = [], []
        columns, filters = [], []
        joins = []

        sources, source_columns = [], []
        for source_name in source_names:
            sources.append({
                'sourceId': source_name,
            })
            source_columns.append({
                'sourceId': source_name,
                'columns': self._get_column_ids(source_name)
            })

        scope = {
            'scopeId': shortuuid.uuid(),
            'columns': columns,
            'joins': joins,

            'sources': sources,
            'sourceColumns': source_columns,
            'filters': filters,
            'categories': categories,
            'measures': measures
        }

        return scope

    def _build_scope(self, scope):
        source_names = self._parquet_data_source.get_sources()

        categories, measures = [], []
        # sources
        sources, source_columns = [], []
        for source_name in source_names:
            sources.append({
                'sourceId': source_name,
            })
            source_columns.append({
                'sourceId': source_name,
                'columns': self._get_column_ids(source_name)
            })

        scope['sources'] = sources
        scope['sourceColumns'] = source_columns
        # joins
        current_joins = scope['joins']
        main_source = scope['source']
        joins = []
        if current_joins and main_source and main_source['sourceId']:
            main_source_id = main_source['sourceId']
            for join in current_joins:
                join_source_id = join['joinSourceId']
                if join_source_id in source_names and not join_source_id == main_source_id:
                    joins.append(join)
                    # append joined columns to categories and measures
                    categories = categories + self._get_category_ids(join_source_id)
                    measures = measures + self._get_measure_ids(join_source_id)

        scope['joins'] = joins
        columns = scope['columns']
        if not columns:
            scope['columns'] = []

        filters = []
        if main_source and main_source['sourceId']:
            main_source_id = main_source['sourceId']
            if main_source_id not in source_names:
                scope.pop('source', None)
            else:
                main_categories = self._get_category_ids(main_source_id)
                filters = filters + main_categories
                categories = categories + main_categories
                measures = measures + self._get_measure_ids(main_source_id)
        # filters
        scope['filters'] = filters
        scope['categories'] = categories
        scope['measures'] = measures

        return scope

    def get_scope(self, dashboard_id: str):
        result = self._mongo_data_source.get_db()[DASHBOARD_COLLECTION].find_one(
            {
                '_id': dashboard_id
            },
            {
                'scope': 1
            })

        if result:
            scope = result.get('scope')
            if scope:
                return self._build_scope(scope)
            else:
                return self._get_empty_scope()
        else:
            return {}

    def update_scope(self, dashboard_id: str, scope: Any):
        updates = []
        for k, v in scope.items():
            updates.append({
                '$set':
                    {
                        'scope.' + k: v
                    }
            })

        updated = self._mongo_data_source.get_db()[DASHBOARD_COLLECTION].find_one_and_update(
            {
                '_id': dashboard_id
            }, updates, return_document=pymongo.ReturnDocument.AFTER)

        if updated:
            scope = updated.get('scope')
            if scope:
                return self._build_scope(scope)
            else:
                return self._get_empty_scope()
        else:
            return {}

    def get_grid(self, dashboard_id: str):
        result = self._mongo_data_source.get_db()[DASHBOARD_COLLECTION].find_one(
            {
                '_id': dashboard_id
            },
            {
                'grid': 1
            })

        if result:
            return result['grid']
        else:
            return {}

    def update_grid(self, dashboard_id: str, grid: Any):
        updates = [
            {
                '$set':
                    {
                        'grid':
                            {
                                '$mergeObjects': ['$grid', grid]
                            }
                    }
            }
        ]

        updated = self._mongo_data_source.get_db()[DASHBOARD_COLLECTION].find_one_and_update(
            {
                '_id': dashboard_id
            }, updates, return_document=pymongo.ReturnDocument.AFTER)

        if updated:
            return updated['grid']
        else:
            return {}

    def get_settings(self, dashboard_id: str):
        result = self._mongo_data_source.get_db()[DASHBOARD_COLLECTION].find_one(
            {
                '_id': dashboard_id
            },
            {
                'settings': 1
            })

        if result:
            return result['settings']
        else:
            return {}
