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

import unittest

import numpy
import pandas as pd

from app.aggregation import pandas_eval_factory
from app.aggregation.aggregation_expr import aggregation_dag

eval_factory = pandas_eval_factory()


class AggregationDAGTest(unittest.TestCase):

    def test_reduction_dag(self):
        """Simple aggregation statement parsing"""
        df = pd.DataFrame({'A': [0, 1, 2, 3, 4],
                           'B': ['Lundi', 'Lundi', 'Mercredi', 'Vendredi', 'Vendredi'],
                           'C': ['Jan', 'Jan', 'Jan', 'Feb', 'Feb']})

        dag = aggregation_dag("SUM('A', EQ('B', \"Lundi\"))")
        evaluator = eval_factory.evaluator('aggregationStatement').build(0, dag)

        result = \
            df.groupby(['B']).apply(
                lambda x: pd.DataFrame({'m': evaluator(x, evaluator.emit_columns())}))

        index = result.index
        result.index = index.droplevel(len(index.names) - 1)
        print(result)

        result = result.reset_index()['m']
        self.assertEqual(len(result), 1)

        self.assertEqual(result[0], 1)

        result = df.groupby(['B', 'C']).apply(
            lambda x: pd.DataFrame({'m': evaluator(x, evaluator.emit_columns())}))
        index = result.index
        result.index = index.droplevel(len(index.names) - 1)
        print(result)
        result = result.reset_index()
        self.assertEqual(len(result), 1)
        m = result['m']
        self.assertEqual(m[0], 1)

        B = result['B']
        self.assertEqual(B[0], 'Lundi')

        C = result['C']
        self.assertEqual(C[0], 'Jan')

    def test_cum_sum(self):
        df = pd.DataFrame({'A': [4, 3, 2, 1, 0],
                           'B': ['Lundi', 'Lundi', 'Mercredi', 'Vendredi', 'Vendredi'],
                           'D': [20, 30, 40, 50, 60]})

        dag = aggregation_dag("CUMSUM(ASC 'A', 'D')")

        evaluator = eval_factory.evaluator('aggregationStatement').build(0, dag)

        result = df.groupby(['B']).apply(lambda x: pd.DataFrame({'m': evaluator(x, evaluator.emit_columns())}))

        print(result)

        result = result.reset_index()
        m = result['m']
        self.assertEqual(m[0], 30)
        self.assertEqual(m[1], 50)
        self.assertEqual(m[2], 40)
        self.assertEqual(m[3], 60)
        self.assertEqual(m[4], 110)

    def test_rol_sum(self):
        df = pd.DataFrame({'A': [4, 3, 2, 1, 0],
                           'B': ['Lundi', 'Lundi', 'Mercredi', 'Vendredi', 'Vendredi'],
                           'D': [20, 30, 40, 50, 60]})

        dag = aggregation_dag("ROLSUM(2, ASC 'A', 'D')")

        evaluator = eval_factory.evaluator('aggregationStatement').build(0, dag)

        result = df.groupby(['B']).apply(lambda x: pd.DataFrame({'m': evaluator(x, evaluator.emit_columns())}))

        print(result)

        result = result.reset_index()
        m = result['m']
        self.assertEqual(m[0], 30)
        self.assertEqual(m[1], 50)
        self.assertEqual(m[2], 40)
        self.assertEqual(m[3], 60)
        self.assertEqual(m[4], 110)

    def test_rol_sum_and_sum_aggr(self):
        df = pd.DataFrame({'A': [4, 3, 2, 1, 27],
                           'T': ["2020-01-01", "2020-01-02", "2020-01-03", "2020-01-04", "2020-01-05"],
                           'B': ['Lundi', 'Lundi', 'Mercredi', 'Vendredi', 'Vendredi'],
                           'D': [20, 30, 40, 50, 60]})

        dag1 = aggregation_dag("SUM('D')")
        dag2 = aggregation_dag("ROLSUM(2, DESC 'T', 'D')")

        evaluator1 = eval_factory.evaluator('aggregationStatement').build(0, dag1)
        evaluator2 = eval_factory.evaluator('aggregationStatement').build(0, dag2)
        index = []
        index += evaluator1.emit_columns()
        index += evaluator2.emit_columns()

        result = df.groupby(['B']).apply(
            lambda x: pd.DataFrame({'m': evaluator1(x, index), 'm2': evaluator2(x, index)}))

        # index = result.index
        # index = index.droplevel(len(index.names)-1)
        # result.index = index

        print(result)
        result = result.reset_index()

        m = result['m2']
        self.assertEqual(m[0], 50.0)
        self.assertEqual(m[1], 30.0)
        self.assertEqual(m[2], 40.0)
        self.assertEqual(m[3], 110.0)
        self.assertEqual(m[4], 60.0)

        m = result['m']
        self.assertEqual(m[0], 20.0)
        self.assertEqual(m[1], 30.0)
        self.assertEqual(m[2], 40.0)
        self.assertEqual(m[3], 50.0)
        self.assertEqual(m[4], 60.0)

    def test_rol_sum_and_sum_aggr_filter(self):
        df = pd.DataFrame({'A': [4, 3, 2, 1, 27],
                           'T': ["2020-01-01", "2020-01-02", "2020-01-03", "2020-01-04", "2020-01-05"],
                           'B': ['Lundi', 'Lundi', 'Mercredi', 'Vendredi', 'Vendredi'],
                           'D': [20, 30, 40, 50, 60]})

        dag1 = aggregation_dag("SUM('D', IN('B', [\"Lundi\",\"Mercredi\"]))")
        dag2 = aggregation_dag("ROLSUM(2, DESC 'T', 'D')")

        evaluator1 = eval_factory.evaluator('aggregationStatement').build(0, dag1)
        evaluator2 = eval_factory.evaluator('aggregationStatement').build(0, dag2)
        index = []
        index += evaluator1.emit_columns()
        index += evaluator2.emit_columns()

        result = df.groupby(['B']).apply(
            lambda x: pd.DataFrame({'m': evaluator1(x, index), 'm2': evaluator2(x, index)}))

        # index = result.index
        # index = index.droplevel(len(index.names)-1)
        # result.index = index

        print(result)
        result = result.reset_index()

        m = result['m2']
        self.assertEqual(m[0], 50.0) # asc order preserved because of sum index
        self.assertEqual(m[1], 30.0)
        self.assertEqual(m[2], 40.0)
        self.assertEqual(m[3], 60.0) # desc
        self.assertEqual(m[4], 110.0)

        m = result['m']
        self.assertEqual(m[0], 20.0)
        self.assertEqual(m[1], 30.0)
        self.assertEqual(m[2], 40.0)
        self.assertTrue(numpy.math.isnan(m[3]))
        self.assertTrue(numpy.math.isnan(m[4]))

    def test_rol_sum_and_count(self):
        df = pd.DataFrame({'A': [4, 3, 2, 1, 27],
                           'T': ["2020-01-01", "2020-01-02", "2020-01-03", "2020-01-04", "2020-01-05"],
                           'B': ['Lundi', 'Lundi', 'Mercredi', 'Vendredi', 'Vendredi'],
                           'D': [20, 30, 40, 50, 60]})

        dag1 = aggregation_dag("COUNT('D')")
        dag3 = aggregation_dag("UCOUNT('D')")
        dag2 = aggregation_dag("ROLSUM(2, DESC 'T', 'D')")

        evaluator1 = eval_factory.evaluator('aggregationStatement').build(0, dag1)
        evaluator2 = eval_factory.evaluator('aggregationStatement').build(0, dag2)
        evaluator23 = eval_factory.evaluator('aggregationStatement').build(0, dag3)
        index = []
        index += evaluator1.emit_columns()
        index += evaluator2.emit_columns()

        result = df.groupby(['B']).apply(
            lambda x: pd.DataFrame(
                {'m': evaluator1(x, index), 'm2': evaluator2(x, index), 'm3': evaluator23(x, index)}))

        # index = result.index
        # index = index.droplevel(len(index.names)-1)
        # result.index = index

        print(result)
        result = result.reset_index()

        m = result['m2']
        self.assertEqual(m[0], 50.0)
        self.assertEqual(m[1], 30.0)
        self.assertEqual(m[2], 40.0)
        self.assertEqual(m[3], 110.0)
        self.assertEqual(m[4], 60.0)

        m = result['m']
        self.assertEqual(m[0], 1)
        self.assertEqual(m[1], 1)
        self.assertEqual(m[2], 1)
        self.assertEqual(m[3], 1)
        self.assertEqual(m[4], 1)

        m = result['m3']
        self.assertEqual(m[0], 1)
        self.assertEqual(m[1], 1)
        self.assertEqual(m[2], 1)
        self.assertEqual(m[3], 1)
        self.assertEqual(m[4], 1)


if __name__ == '__main__':
    unittest.main()
