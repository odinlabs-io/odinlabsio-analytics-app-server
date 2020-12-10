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

import pyarrow.dataset as ds

from app.aggregation.evaldag import ConditionStatement, ConditionBinOp, ConditionGroup, ConditionNegate, \
    IdentityCondition, SelectorOrder, SelectorIn, ReferenceCategory, Literals, FloatLiteral, StringLiteral


class PyArrowConditionStatement(ConditionStatement):
    def __init__(self):
        super().__init__()

    def __call__(self):
        return self._condition()


class PyArrowConditionBinOp(ConditionBinOp):
    def __init__(self):
        super().__init__()

    def __call__(self):
        left = self._condition_left()
        right = self._condition_right()

        operator = self._condition_operator

        if operator == 'AND':
            return left & right
        if operator == 'OR':
            return left | right


class PyArrowConditionGroup(ConditionGroup):
    def __init__(self):
        super().__init__()

    def __call__(self):
        return self._condition()


class PyArrowConditionNegate(ConditionNegate):
    def __init__(self):
        super().__init__()

    def __call__(self):
        return ~self._condition()


class PyArrowIdentityCondition(IdentityCondition):
    def __init__(self):
        super().__init__()

    def __call__(self):
        return self._selector()


class PyArrowSelectorOrder(SelectorOrder):
    def __init__(self):
        super().__init__()

    def __call__(self):
        category = self._category()
        value = self.solvers[self._category.input_columns()[0]].solve_for_variable(self._literal())

        order_operator = self._order_operator
        if order_operator == 'EQ':
            return category == value
        if order_operator == 'GT':
            return category > value
        if order_operator == 'GTE':
            return category >= value
        if order_operator == 'LT':
            return category < value
        if order_operator == 'LTE':
            return category <= value


class PyArrowSelectorIn(SelectorIn):
    def __init__(self):
        super().__init__()

    def __call__(self):
        values = self._solvers[self._category.input_columns()[0]].solve_for_variable(self._literals())

        return self._category().isin(values)


class PyArrowReferenceCategory(ReferenceCategory):
    def __init__(self):
        super().__init__()

    def __call__(self):
        return ds.field(self._id_literal)


class PyArrowValues(Literals):
    def __init__(self):
        super().__init__()

    def __call__(self):
        return [value() for value in self._literals]


class PyArrowFloatLiteral(FloatLiteral):
    def __init__(self):
        super().__init__()

    def __call__(self):
        return self._float_literal


class PyArrowStringLiteral(StringLiteral):
    def __init__(self):
        super().__init__()

    def __call__(self):
        return self._literal
