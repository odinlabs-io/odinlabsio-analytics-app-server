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

import functools
from typing import List

import numpy as np
import pandas as pd
from pandas import DataFrame

from app.aggregation.evaldag import AggregationStatement, AggregationBinOp, AggregationGroup, Reduction, \
    IdentityAggregation, ExpressionBinOp, ExpressionGroup, IdentityExpression, ConditionStatement, ConditionBinOp, \
    ConditionGroup, ConditionNegate, IdentityCondition, SelectorOrder, SelectorIn, ConstantMeasure, ReferenceMeasure, \
    ReferenceCategory, Literals, StringLiteral, Count, FloatLiteral, CumReduction, RolReduction


class PandasAggregationStatement(AggregationStatement):
    def __init__(self):
        super().__init__()

    def __call__(self, df: DataFrame, index: List[str]):
        return self._aggregation(df, index)


class PandasAggregationBinOp(AggregationBinOp):
    def __init__(self):
        super().__init__()

    def __call__(self, df: DataFrame, index: List[str]):
        left = self._aggregation_left(df, index)
        right = self._aggregation_right(df, index)
        operator = self._aggregation_operator

        if operator == '+':
            return left + right
        elif operator == '-':
            return left - right
        elif operator == '*':
            return left * right
        elif operator == '/':
            return left / right
        else:
            raise 'Unknown operator {}'.format(operator)


class PandasAggregationGroup(AggregationGroup):
    def __init__(self):
        super().__init__()

    def __call__(self, df: DataFrame, index: List[str]):
        return self._aggregation(df, index)


class PandasReduction(Reduction):
    def __init__(self):
        super().__init__()

    def __call__(self, df: DataFrame, index: List[str]):
        if len(self._conditions) > 0:
            condition = functools.reduce(lambda x, y: x & y, [cond(df, index) for cond in self._conditions])
            filtered_df = df.loc[condition]
        else:
            filtered_df = df
        if len(filtered_df) == 0:
            if index and len(index) > 0:
                return pd.Series([], dtype=np.float64)
            else:
                return pd.Series([], dtype=np.float64)

        expression = self._expression(filtered_df, index)
        if index and len(index) > 0:
            for ind in index:
                expression[ind] = filtered_df.loc[:, ind]
            expression = expression.groupby(index)

        reduction = self._reduction_operator

        if reduction == 'SUM':
            value = expression.sum()
        elif reduction == 'PROD':
            value = expression.prod()
        elif reduction == 'MAX':
            value = expression.max()
        elif reduction == 'MIN':
            value = expression.min()
        elif reduction == 'AVG':
            value = expression.mean()
        elif reduction == 'VAR':
            value = expression.var()
        elif reduction == 'STD':
            value = expression.std()
        else:
            raise 'Unknown reduction operator {}'.format(reduction)

        return pd.Series(value.values, index=value.index) if index and len(index) > 0 else pd.Series(value)


class PandasCumReduction(CumReduction):
    def __init__(self):
        super().__init__()

    def __call__(self, df: DataFrame, index: List[str]):
        if index and len(index) > 0:
            if not index == self.emit_columns():
                raise Exception('Index does not match emited columns')

        if len(self._conditions) > 0:
            condition = functools.reduce(lambda x, y: x & y, [cond(df, index) for cond in self._conditions])
            filtered_df = df.loc[condition]
        else:
            filtered_df = df

        if self._sort == 'ASC':
            filtered_df = filtered_df.sort_values([self._category], ascending=True)
        else:
            filtered_df = filtered_df.sort_values([self._category], ascending=False)

        expression = self._expression(filtered_df, index)

        reduction = self._cum_reduction_operator

        if reduction == 'CUMSUM':
            values = expression.cumsum().values
        elif reduction == 'CUMPROD':
            values = expression.cumprod().values
        elif reduction == 'CUMMAX':
            values = expression.cummax().values
        elif reduction == 'CUMMIN':
            values = expression.cummin().values
        else:
            raise 'Unknown reduction operator {}'.format(reduction)

        return pd.Series(values, index=filtered_df[self._category])


class PandasRolReduction(RolReduction):
    def __init__(self):
        super().__init__()

    def __call__(self, df: DataFrame, index: List[str]):
        if index and len(index) > 0:
            if not index == self.emit_columns():
                raise Exception('Index does not match emited columns')

        if len(self._conditions) > 0:
            condition = functools.reduce(lambda x, y: x & y, [cond(df, index) for cond in self._conditions])
            filtered_df = df.loc[condition]
        else:
            filtered_df = df

        if self._sort == 'ASC':
            filtered_df = filtered_df.sort_values([self._category], ascending=True)
        else:
            filtered_df = filtered_df.sort_values([self._category], ascending=False)

        expression = self._expression(filtered_df, index).rolling(self._window, min_periods=1)

        reduction = self._rol_reduction_operator

        if reduction == 'ROLSUM':
            values = expression.sum().values
        elif reduction == 'ROLPROD':
            values = expression.prod().values
        elif reduction == 'ROLMAX':
            values = expression.max().values
        elif reduction == 'ROLMIN':
            values = expression.min().values
        else:
            raise 'Unknown reduction operator {}'.format(reduction)

        return pd.Series(values, index=filtered_df[self._category])


class PandasCount(Count):
    def __init__(self):
        super().__init__()

    def __call__(self, df: DataFrame, index: List[str]):
        if len(self._conditions) > 0:
            condition = functools.reduce(lambda x, y: x & y, [cond(df, index) for cond in self._conditions])
            filtered_df = df.loc[condition]
        else:
            filtered_df = df

        category = self._category(filtered_df, index)
        if index and len(index) > 0:
            for ind in index:
                category[ind] = filtered_df.loc[:, ind]
            category = category.groupby(index)

        count = self._count_operator

        if count == 'COUNT':
            value = category.count()
        elif count == 'UCOUNT':
            value = len(category.unique()) if not index else category.apply(lambda x: len(x.unique()))
        else:
            raise 'Unknown count operator {}'.format(count)

        return pd.Series(value)


class PandasIdentityAggregation(IdentityAggregation):
    def __init__(self):
        super().__init__()

    def __call__(self, df: DataFrame, index: List[str]):
        return self._expression(df, index)


class PandasExpressionBinOp(ExpressionBinOp):
    def __init__(self):
        super().__init__()

    def __call__(self, df: DataFrame, index: List[str]):
        left = self._expression_left(df, index)
        right = self._expression_right(df, index)

        operator = self._expression_operator

        if operator == '+':
            return left + right
        elif operator == '-':
            return left - right
        elif operator == '*':
            return left * right
        elif operator == '/':
            return left / right
        else:
            raise 'Unknown arithmetic operator {}'.format(operator)


class PandasExpressionGroup(ExpressionGroup):
    def __init__(self):
        super().__init__()

    def __call__(self, df: DataFrame, index: List[str]):
        return self._expression(df, index)


class PandasIdentityExpression(IdentityExpression):
    def __init__(self):
        super().__init__()

    def __call__(self, df: DataFrame, index: List[str]):
        return self._measure(df, index)


class PandasConditionStatement(ConditionStatement):
    def __init__(self):
        super().__init__()

    def __call__(self, df: DataFrame, index: List[str]):
        return self._condition(df, index)


class PandasConditionBinOp(ConditionBinOp):
    def __init__(self):
        super().__init__()

    def __call__(self, df: DataFrame, index: List[str]):
        left = self._condition_left(df, index)
        right = self._condition_right(df, index)

        operator = self._condition_operator

        if operator == 'AND':
            return left & right
        elif operator == 'OR':
            return left | right
        else:
            raise 'Unknown set operator {}'.format(operator)


class PandasConditionGroup(ConditionGroup):
    def __init__(self):
        super().__init__()

    def __call__(self, df: DataFrame, index: List[str]):
        return self._condition(df, index)


class PandasConditionNegate(ConditionNegate):
    def __init__(self):
        super().__init__()

    def __call__(self, df: DataFrame, index: List[str]):
        return ~self._condition(df, index)


class PandasIdentityCondition(IdentityCondition):
    def __init__(self):
        super().__init__()

    def __call__(self, df: DataFrame, index: List[str]):
        return self._selector(df, index)


class PandasSelectorOrder(SelectorOrder):
    def __init__(self):
        super().__init__()

    def __call__(self, df: DataFrame, index: List[str]):
        category = self._category(df, index)
        value = self.solvers[self._category.input_columns()[0]].solve_for_variable(self._literal(df, index))

        order_operator = self._order_operator
        if order_operator == 'EQ':
            return category == value
        elif order_operator == 'GT':
            return category.gt(value)
        elif order_operator == 'GTE':
            return category.ge(value)
        elif order_operator == 'LT':
            return category.lt(value)
        elif order_operator == 'LTE':
            return category.le(value)
        else:
            raise 'Unknown order operator {}'.format(order_operator)


class PandasSelectorIn(SelectorIn):
    def __init__(self):
        super().__init__()

    def __call__(self, df: DataFrame, index: List[str]):
        values = self._solvers[self._category.input_columns()[0]].solve_for_variable(self._literals(df, index))

        return self._category(df, index).isin(values)


class PandasConstantMeasure(ConstantMeasure):
    def __init__(self):
        super().__init__()

    def __call__(self, df: DataFrame, index: List[str]):
        return self._literal


class PandasReferenceMeasure(ReferenceMeasure):
    def __init__(self):
        super().__init__()

    def __call__(self, df: DataFrame, index: List[str]):
        return df[self._id_literal]


class PandasReferenceCategory(ReferenceCategory):
    def __init__(self):
        super().__init__()

    def __call__(self, df: DataFrame, index: List[str]):
        return df[self._id_literal]


class PandasLiterals(Literals):
    def __init__(self):
        super().__init__()

    def __call__(self, df: DataFrame, index: List[str]):
        return [value(df, index) for value in self._literals]


class PandasFloatLiteral(FloatLiteral):
    def __init__(self):
        super().__init__()

    def __call__(self, df: DataFrame, index: List[str]):
        return self._float_literal


class PandasStringLiteral(StringLiteral):
    def __init__(self):
        super().__init__()

    def __call__(self, df: DataFrame, index: List[str]):
        return self._literal
