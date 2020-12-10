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
from datetime import datetime

import numpy as np
import pandas as pd

from app.aggregation import pandas_eval_factory
from app.aggregation.aggregation_expr import aggregation_dag, filter_dag
from app.aggregation.pandassolver import DateSolver

eval_factory = pandas_eval_factory()
eval_factory.add_solver('Time', DateSolver())


class PandasAggregationEvalTest(unittest.TestCase):

    def test_reduction(self):
        df = pd.DataFrame({'A': [0, 1, 2, 3, 4]})

        index = []
        dag = aggregation_dag("SUM('A')")

        self.assertEqual(eval_factory.evaluator('aggregationStatement').build(0, dag)(df, index)[0], 10)

        dag = aggregation_dag("PROD('A')")

        self.assertEqual(eval_factory.evaluator('aggregationStatement').build(0, dag)(df, index)[0], 0)

        dag = aggregation_dag("MAX('A')")

        self.assertEqual(eval_factory.evaluator('aggregationStatement').build(0, dag)(df, index)[0], 4)

        dag = aggregation_dag("MIN('A')")

        self.assertEqual(eval_factory.evaluator('aggregationStatement').build(0, dag)(df, index)[0], 0)

        dag = aggregation_dag("AVG('A')")

        self.assertEqual(eval_factory.evaluator('aggregationStatement').build(0, dag)(df, index)[0], 2)

        dag = aggregation_dag("VAR('A')")

        self.assertEqual(eval_factory.evaluator('aggregationStatement').build(0, dag)(df, index)[0],
                         2.5)

    def test_count(self):
        index = []
        df = pd.DataFrame({'A': [0, 1, 2, 3, 4], 'B': ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi']})

        dag = aggregation_dag("COUNT('B')")

        self.assertEqual(eval_factory.evaluator('aggregationStatement').build(0, dag)(df, index)[0], 5)

    def test_ucount(self):
       
        df = pd.DataFrame({'B': ['Lundi', 'Lundi', 'Mercredi', 'Mercredi', 'Vendredi']})

        dag = aggregation_dag("UCOUNT('B')")

        index = []
        self.assertEqual(eval_factory.evaluator('aggregationStatement').build(0, dag)(df,index)[0], 3)

    def test_reduction_condition(self):
        df = pd.DataFrame({'A': [0, 1, 2, 3, 4], 'B': ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi']})

        index = []
        dag = aggregation_dag("SUM('A', EQ('B', \"Lundi\"))")

        self.assertEqual(eval_factory.evaluator('aggregationStatement').build(0, dag)(df,index)[0], 0)

        dag = aggregation_dag("SUM('A', IN('B', [\"Lundi\",\"Mardi\"]))")

        self.assertEqual(eval_factory.evaluator('aggregationStatement').build(0, dag)(df,index)[0], 1)

    def test_arithmetic_aggregation(self):
        df = pd.DataFrame({'A': [0, 1, 2, 3, 4], 'B': [4, 3, 2, 1, 0]})

        index = []
        dag = aggregation_dag("SUM('A')+SUM('B')")
        self.assertEqual(eval_factory.evaluator('aggregationStatement').build(0, dag)(df,index)[0],
                         4 * 5)

        dag = aggregation_dag("SUM('A')-SUM('B')")
        self.assertEqual(eval_factory.evaluator('aggregationStatement').build(0, dag)(df,index)[0], 0)

        dag = aggregation_dag("SUM('A')*SUM('B')")
        self.assertEqual(eval_factory.evaluator('aggregationStatement').build(0, dag)(df,index)[0],
                         100)

        dag = aggregation_dag("SUM('A')/SUM('B')")
        self.assertEqual(eval_factory.evaluator('aggregationStatement').build(0, dag)(df,index)[0],
                         1.0)

        dag = aggregation_dag("SUM('A') / 10")
        self.assertEqual(eval_factory.evaluator('aggregationStatement').build(0, dag)(df,index)[0],
                         1)

        dag = aggregation_dag("SUM('A') * 10")
        self.assertEqual(eval_factory.evaluator('aggregationStatement').build(0, dag)(df,index)[0],
                         100)

        dag = aggregation_dag("SUM('A') - 10")
        self.assertEqual(eval_factory.evaluator('aggregationStatement').build(0, dag)(df,index)[0],
                         0)

        dag = aggregation_dag("SUM('A') + 10")
        self.assertEqual(eval_factory.evaluator('aggregationStatement').build(0, dag)(df,index)[0],
                         20)

    def test_arithmetic_measure(self):
        df = pd.DataFrame({'A': [0, 1, 2, 3, 4], 'B': [4, 3, 2, 1, 0]})

        index = []
        
        dag = aggregation_dag("SUM('A' + 'B')")
        self.assertEqual(eval_factory.evaluator('aggregationStatement').build(0, dag)(df,index)[0],
                         4 * 5)

        dag = aggregation_dag("SUM('A' - 'B')")
        self.assertEqual(eval_factory.evaluator('aggregationStatement').build(0, dag)(df,index)[0], 0)

        dag = aggregation_dag("SUM('A' * 'B')")
        self.assertEqual(eval_factory.evaluator('aggregationStatement').build(0, dag)(df,index)[0], 10)

        dag = aggregation_dag("SUM('A' / 'B')")
        self.assertEqual(eval_factory.evaluator('aggregationStatement').build(0, dag)(df,index)[0],
                         float('inf'))

        dag = aggregation_dag("SUM('A' + 1)")
        self.assertEqual(eval_factory.evaluator('aggregationStatement').build(0, dag)(df,index)[0], 15)

        dag = aggregation_dag("SUM('A' - 1)")
        self.assertEqual(eval_factory.evaluator('aggregationStatement').build(0, dag)(df,index)[0], 5)

        dag = aggregation_dag("SUM('A' * 2)")
        self.assertEqual(eval_factory.evaluator('aggregationStatement').build(0, dag)(df,index)[0], 20)

        dag = aggregation_dag("SUM('A' / 1)")
        self.assertEqual(eval_factory.evaluator('aggregationStatement').build(0, dag)(df,index)[0],
                         10)

    def test_filter(self):
        df = pd.DataFrame({'A': [0, 1, 2, 3, 4], 'B': ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi'],
                           'C': ['Jan', 'Feb', 'March', 'April', 'May']})

        index = []
        
        dag = filter_dag("EQ('A', 0)")
        self.assertEqual(
            (eval_factory.evaluator('conditionStatement').build(0, dag)(df,index) ^ pd.Series(
                [True, False, False, False, False])).sum(), 0)

        dag = filter_dag("GT('A', 0)")
        self.assertEqual(
            (eval_factory.evaluator('conditionStatement').build(0, dag)(df,index) ^ pd.Series(
                [False, True, True, True, True])).sum(), 0)

        dag = filter_dag("GTE('A', 0)")
        self.assertEqual(
            (eval_factory.evaluator('conditionStatement').build(0, dag)(df,index) ^ pd.Series(
                [True, True, True, True, True])).sum(), 0)

        dag = filter_dag("LT('A', 0)")
        self.assertEqual(
            (eval_factory.evaluator('conditionStatement').build(0, dag)(df,index) ^ pd.Series(
                [False, False, False, False, False])).sum(), 0)

        dag = filter_dag("LTE('A', 0)")
        self.assertEqual(
            (eval_factory.evaluator('conditionStatement').build(0, dag)(df,index) ^ pd.Series(
                [True, False, False, False, False])).sum(), 0)

        dag = filter_dag("EQ('B', \"Lundi\")")
        self.assertEqual(
            (eval_factory.evaluator('conditionStatement').build(0, dag)(df,index) ^ pd.Series(
                [True, False, False, False, False])).sum(), 0)

        dag = filter_dag("EQ('B', \"Lundi\") AND EQ('C', \"Jan\")")
        self.assertEqual(
            (eval_factory.evaluator('conditionStatement').build(0, dag)(df,index) ^ pd.Series(
                [True, False, False, False, False])).sum(), 0)

        dag = filter_dag("EQ('B', \"Lundi\") AND EQ('C', \"Feb\")")
        self.assertEqual(
            (eval_factory.evaluator('conditionStatement').build(0, dag)(df,index) ^ pd.Series(
                [False, False, False, False, False])).sum(), 0)

        dag = filter_dag("EQ('B', \"Lundi\") OR EQ('B', \"Mardi\")")
        self.assertEqual(
            (eval_factory.evaluator('conditionStatement').build(0, dag)(df,index) ^ pd.Series(
                [True, True, False, False, False])).sum(), 0)

        dag = filter_dag("IN('A', [0,1])")
        self.assertEqual(
            (eval_factory.evaluator('conditionStatement').build(0, dag)(df,index) ^ pd.Series(
                [True, True, False, False, False])).sum(), 0)

        dag = filter_dag("IN('B', [\"Lundi\",\"Mardi\"])")
        self.assertEqual(
            (eval_factory.evaluator('conditionStatement').build(0, dag)(df,index) ^ pd.Series(
                [True, True, False, False, False])).sum(), 0)

    def test_variables(self):
        dag = aggregation_dag("SUM('A', EQ('X', 10)) + SUM('B', IN('Y',[1,2])) / 'A'")
    
        evaluator = eval_factory.evaluator('aggregationStatement').build(0, dag)

        variables = set(evaluator.input_columns())

        self.assertEqual(len(variables), 4)
        self.assertSetEqual(set(variables), {'A', 'B', 'X', 'Y'})

    def test_solvers(self):
        index = []
        
        df = pd.DataFrame({'Time': [datetime(2020, 1, 1), datetime(2018, 1, 2), datetime(2018, 1, 3),
                                    datetime(2018, 1, 4), datetime(2018, 1, 5)]})

        dag = filter_dag("EQ('Time', \"2020-01-01\")")

        self.assertEqual(
            (eval_factory.evaluator('conditionStatement').build(0, dag)(df,index) ^ pd.Series(
                [True, False, False, False, False])).sum(), 0)

        df = pd.DataFrame({'Time': [np.datetime64('today') - 2, np.datetime64('today') - 1, np.datetime64('today'),
                                    np.datetime64('today') + 1, np.datetime64('today') + 2]})

        dag = filter_dag("EQ('Time', \"today\")")

        self.assertEqual(
            (eval_factory.evaluator('conditionStatement').build(0, dag)(df,index) ^ pd.Series(
                [False, False, True, False, False])).sum(), 0)


if __name__ == '__main__':
    unittest.main()
