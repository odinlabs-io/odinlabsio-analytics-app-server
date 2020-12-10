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

from app.aggregation.dag import EvalNode, DAG


class AggregationStatement(EvalNode):
    def __init__(self):
        super().__init__(rule='aggregationStatement', ctx='AggregationStatementContext')
        self._aggregation = None

    def parser(self, current_node: int, dag: DAG):
        children = dag.children(current_node)
        if len(children) != 2:
            raise Exception('Expected Aggregation and EOF for rule AggregationStatementContext')

        child_id_0 = children[0]
        self._aggregation = self.factory.evaluator('aggregation').build(child_id_0, dag)

        return self

    def input_columns(self):
        return self._aggregation.input_columns()

    def emit_columns(self):
        return self._aggregation.emit_columns()


class AggregationBinOp(EvalNode):
    def __init__(self):
        super().__init__(rule='aggregation', ctx='AggregationBinOpContext')
        self._aggregation_left = None
        self._aggregation_right = None
        self._aggregation_operator = None

    def parser(self, current_node: int, dag: DAG):
        children = dag.children(current_node)
        if len(children) != 3:
            raise Exception('Expected Left Operator Right')

        child_id_0 = children[0]
        child_id_1 = children[1]
        child_id_2 = children[2]

        self._aggregation_left = self.factory.evaluator('aggregation').build(child_id_0, dag)
        self._aggregation_right = self.factory.evaluator('aggregation').build(child_id_2, dag)

        self._aggregation_operator = dag.attr(child_id_1)['value']

        return self

    def input_columns(self):
        return self._aggregation_left.input_columns() + self._aggregation_right.input_columns()

    def emit_columns(self):
        return self._aggregation_left.emit_columns() + self._aggregation_right.emit_columns()


class AggregationGroup(EvalNode):
    def __init__(self):
        super().__init__(rule='aggregation', ctx='AggregationGroupContext')
        self._aggregation = None

    def parser(self, current_node: int, dag: DAG):
        children = dag.children(current_node)
        if len(children) != 3:
            raise Exception('Expected Group Aggregation')

        child_id_1 = children[1]

        self._aggregation = self.factory.evaluator('aggregation').build(child_id_1, dag)

        return self

    def input_columns(self):
        return self._aggregation.input_columns()

    def emit_columns(self):
        return self._aggregation.emit_columns()


class Reduction(EvalNode):
    def __init__(self):
        super().__init__(rule='aggregation', ctx='ReductionContext')
        self._reduction_operator = None
        self._expression = None
        self._conditions = []

    def parser(self, current_node: int, dag: DAG):
        children = dag.children(current_node)
        if len(children) < 4:
            raise Exception('Expected Reduction Expression')

        child_id_0 = children[0]
        child_id_2 = children[2]

        self._reduction_operator = dag.attr(child_id_0)['value']
        self._expression = self.factory.evaluator('expression').build(child_id_2, dag)

        for i in range(4, len(children) - 1, 2):
            condition = children[i]
            self._conditions.append(self.factory.evaluator('condition').build(condition, dag))

        return self

    def input_columns(self):
        return [var for condition in self._conditions for var in
                condition.input_columns()] + self._expression.input_columns()

    def emit_columns(self):
        return []


class CumReduction(EvalNode):
    def __init__(self):
        super().__init__(rule='aggregation', ctx='CumReductionContext')
        self._cum_reduction_operator = None
        self._sort = None
        self._category = None
        self._expression = None
        self._conditions = []

    def parser(self, current_node: int, dag: DAG):
        children = dag.children(current_node)
        if len(children) < 7:
            raise Exception('Expected CumReduction Expression')

        child_id_0 = children[0]
        child_id_2 = children[2]
        child_id_3 = children[3]
        child_id_5 = children[5]

        self._cum_reduction_operator = dag.attr(child_id_0)['value']
        self._sort = dag.attr(child_id_2)['value']
        self._category = dag.attr(child_id_3)['value'][1:-1]
        self._expression = self.factory.evaluator('expression').build(child_id_5, dag)

        for i in range(7, len(children) - 1, 2):
            condition = children[i]
            self._conditions.append(self.factory.evaluator('condition').build(condition, dag))

        return self

    def input_columns(self):
        return [var for condition in self._conditions for var in
                condition.input_columns()] + self._expression.input_columns() + self._category.input_columns()

    def emit_columns(self):
        return [self._category]


class RolReduction(EvalNode):
    def __init__(self):
        super().__init__(rule='aggregation', ctx='RolReductionContext')
        self._rol_reduction_operator = None
        self._window = None
        self._sort = None
        self._category = None
        self._expression = None
        self._conditions = []

    def parser(self, current_node: int, dag: DAG):
        children = dag.children(current_node)
        if len(children) < 9:
            raise Exception('Expected RolReduction Expression')

        child_id_0 = children[0]
        child_id_2 = children[2]
        child_id_4 = children[4]
        child_id_5 = children[5]
        child_id_7 = children[7]

        self._rol_reduction_operator = dag.attr(child_id_0)['value']
        self._window = int(dag.attr(child_id_2)['value'])
        self._sort = dag.attr(child_id_4)['value']
        self._category = dag.attr(child_id_5)['value'][1:-1]
        self._expression = self.factory.evaluator('expression').build(child_id_7, dag)

        for i in range(9, len(children) - 1, 2):
            condition = children[i]
            self._conditions.append(self.factory.evaluator('condition').build(condition, dag))

        return self

    def input_columns(self):
        return [var for condition in self._conditions for var in
                condition.input_columns()] + self._expression.input_columns() + self._category.input_columns()

    def emit_columns(self):
        return [self._category]


class Count(EvalNode):
    def __init__(self):
        super().__init__(rule='aggregation', ctx='CountContext')
        self._count_operator = None
        self._category = None
        self._conditions = []

    def parser(self, current_node: int, dag: DAG):
        children = dag.children(current_node)
        if len(children) < 4:
            raise Exception('Expected Reduction Expression')

        child_id_0 = children[0]
        child_id_2 = children[2]

        self._count_operator = dag.attr(child_id_0)['value']
        self._category = self.factory.evaluator('category').build(child_id_2, dag)

        for i in range(4, len(children) - 1, 2):
            condition = children[i]
            self._conditions.append(self.factory.evaluator('condition').build(condition, dag))

        return self

    def input_columns(self):
        return [var for condition in self._conditions for var in
                condition.input_columns()] + self._category.input_columns()

    def emit_columns(self):
        return []


class IdentityAggregation(EvalNode):
    def __init__(self):
        super().__init__(rule='aggregation', ctx='IdentityAggregationContext')
        self._expression = None

    def parser(self, current_node: int, dag: DAG):
        children = dag.children(current_node)
        if len(children) != 1:
            raise Exception('Expected Expression')

        child_id_0 = children[0]

        self._expression = self.factory.evaluator('expression').build(child_id_0, dag)

        return self

    def input_columns(self):
        return self._expression.input_columns()

    def emit_columns(self):
        return []


class ExpressionBinOp(EvalNode):
    def __init__(self):
        super().__init__(rule='expression', ctx='ExpressionBinOpContext')
        self._expression_left = None
        self._expression_right = None
        self._expression_operator = None

    def parser(self, current_node: int, dag: DAG):
        children = dag.children(current_node)
        if len(children) != 3:
            raise Exception('Expected Left Operator Right')

        child_id_0 = children[0]
        child_id_1 = children[1]
        child_id_2 = children[2]

        self._expression_left = self.factory.evaluator('expression').build(child_id_0, dag)
        self._expression_right = self.factory.evaluator('expression').build(child_id_2, dag)

        self._expression_operator = dag.attr(child_id_1)['value']

        return self

    def input_columns(self):
        return self._expression_left.input_columns() + self._expression_right.input_columns()

    def emit_columns(self):
        return []


class ExpressionGroup(EvalNode):
    def __init__(self):
        super().__init__(rule='expression', ctx='ExpressionGroupContext')
        self._expression = None

    def parser(self, current_node: int, dag: DAG):
        children = dag.children(current_node)
        if len(children) != 3:
            raise Exception('Expected Group Expression')

        child_id_1 = children[1]

        self._expression = self.factory.evaluator('expression').build(child_id_1, dag)

        return self

    def input_columns(self):
        return self._expression.input_columns()

    def emit_columns(self):
        return []


class IdentityExpression(EvalNode):
    def __init__(self):
        super().__init__(rule='expression', ctx='IdentityExpressionContext')
        self._measure = None

    def parser(self, current_node: int, dag: DAG):
        children = dag.children(current_node)
        if len(children) != 1:
            raise Exception('Expected Measure')

        child_id_0 = children[0]

        self._measure = self.factory.evaluator('measure').build(child_id_0, dag)

        return self

    def input_columns(self):
        return self._measure.input_columns()

    def emit_columns(self):
        return []


class ConditionStatement(EvalNode):
    def __init__(self):
        super().__init__(rule='conditionStatement', ctx='ConditionStatementContext')
        self._condition = None

    def parser(self, current_node: int, dag: DAG):
        children = dag.children(current_node)
        if len(children) != 2:
            raise Exception('Expected Condition and EOF for rule ConditionStatementContext')

        child_0 = children[0]
        self._condition = self.factory.evaluator('condition').build(child_0, dag)

        return self

    def input_columns(self):
        return self._condition.input_columns()

    def emit_columns(self):
        return []


class ConditionBinOp(EvalNode):
    def __init__(self):
        super().__init__(rule='condition', ctx='ConditionBinOpContext')
        self._condition_left = None
        self._condition_right = None
        self._condition_operator = None

    def parser(self, current_node: int, dag: DAG):
        children = dag.children(current_node)
        if len(children) != 3:
            raise Exception('Expected Left Operator Right')

        child_id_0 = children[0]
        child_id_1 = children[1]
        child_id_2 = children[2]

        self._condition_left = self.factory.evaluator('condition').build(child_id_0, dag)
        self._condition_right = self.factory.evaluator('condition').build(child_id_2, dag)

        self._condition_operator = dag.attr(child_id_1)['value']

        return self

    def input_columns(self):
        return self._condition_left.input_columns() + self._condition_right.input_columns()

    def emit_columns(self):
        return []


class ConditionGroup(EvalNode):
    def __init__(self):
        super().__init__(rule='condition', ctx='ConditionGroupContext')
        self._condition = None

    def parser(self, current_node: int, dag: DAG):
        children = dag.children(current_node)
        if len(children) != 3:
            raise Exception('Expected Group Condition')

        child_id_1 = children[1]

        self._condition = self.factory.evaluator('condition').build(child_id_1, dag)

        return self

    def input_columns(self):
        return self._condition.input_columns()

    def emit_columns(self):
        return []


class ConditionNegate(EvalNode):
    def __init__(self):
        super().__init__(rule='condition', ctx='ConditionNegateContext')
        self._condition = None

    def parser(self, current_node: int, dag: DAG):
        children = dag.children(current_node)
        if len(children) != 4:
            raise Exception('Expected Group Condition')

        child_id_2 = children[2]

        self._condition = self.factory.evaluator('condition').build(child_id_2, dag)

        return self

    def input_columns(self):
        return self._condition.input_columns()

    def emit_columns(self):
        return []


class IdentityCondition(EvalNode):
    def __init__(self):
        super().__init__(rule='condition', ctx='IdentityConditionContext')
        self._selector = None

    def parser(self, current_node: int, dag: DAG):
        children = dag.children(current_node)
        if len(children) != 1:
            raise Exception('Expected Selector')

        child_id_0 = children[0]

        self._selector = self.factory.evaluator('selector').build(child_id_0, dag)

        return self

    def input_columns(self):
        return self._selector.input_columns()

    def emit_columns(self):
        return []


class SelectorOrder(EvalNode):
    def __init__(self):
        super().__init__(rule='selector', ctx='SelectorOrderContext')
        self._order_operator = None
        self._category = None
        self._literal = None

    def parser(self, current_node: int, dag: DAG):
        children = dag.children(current_node)
        if len(children) != 6:
            raise Exception('Expected Order Selector')

        child_id_0 = children[0]
        child_id_2 = children[2]
        child_id_4 = children[4]

        self._order_operator = dag.attr(child_id_0)['value']
        self._category = self.factory.evaluator('category').build(child_id_2, dag)
        self._literal = self.factory.evaluator('literal').build(child_id_4, dag)

        return self

    def input_columns(self):
        return self._category.input_columns() + self._literal.input_columns()

    def emit_columns(self):
        return []


class SelectorIn(EvalNode):
    def __init__(self):
        super().__init__(rule='selector', ctx='SelectorInContext')
        self._category = None
        self._literals = None

    def parser(self, current_node: int, dag: DAG):
        children = dag.children(current_node)
        if len(children) != 6:
            raise Exception('Expected In Selector')

        child_id_2 = children[2]
        child_id_4 = children[4]

        self._category = self.factory.evaluator('category').build(child_id_2, dag)
        self._literals = self.factory.evaluator('literals').build(child_id_4, dag)

        return self

    def input_columns(self):
        return self._category.input_columns() + self._literals.input_columns()

    def emit_columns(self):
        return []


class ConstantMeasure(EvalNode):
    def __init__(self):
        super().__init__(rule='measure', ctx='ConstantMeasureContext')
        self._literal = None

    def parser(self, current_node: int, dag: DAG):
        children = dag.children(current_node)
        if len(children) != 1:
            raise Exception('Expected Measure')

        child_id_0 = children[0]

        self._literal = float(dag.attr(child_id_0)['value'])

        return self

    def input_columns(self):
        return []

    def emit_columns(self):
        return []


class ReferenceMeasure(EvalNode):
    def __init__(self):
        super().__init__(rule='measure', ctx='ReferenceMeasureContext')
        self._id_literal = None

    def parser(self, current_node: int, dag: DAG):
        children = dag.children(current_node)
        if len(children) != 1:
            raise Exception('Expected Measure')

        child_id_0 = children[0]

        self._id_literal = dag.attr(child_id_0)['value'][1:-1]

        return self

    def input_columns(self):
        return [self._id_literal]

    def emit_columns(self):
        return []


class ReferenceCategory(EvalNode):
    def __init__(self):
        super().__init__(rule='category', ctx='ReferenceCategoryContext')
        self._id_literal = None

    def parser(self, current_node: int, dag: DAG):
        children = dag.children(current_node)
        if len(children) != 1:
            raise Exception('Expected Category')

        child_id_0 = children[0]

        self._id_literal = dag.attr(child_id_0)['value'][1:-1]

        return self

    def input_columns(self):
        return [self._id_literal]

    def emit_columns(self):
        return []


class Literals(EvalNode):
    def __init__(self):
        super().__init__(rule='literals', ctx='LiteralsContext')
        self._literals = []

    def parser(self, current_node: int, dag: DAG):
        children = dag.children(current_node)
        if len(children) < 3:
            raise Exception('Expected Values')

        for i in range(1, len(children) - 1, 2):
            self._literals.append(self.factory.evaluator('literal').build(children[i], dag))

        return self

    def input_columns(self):
        return [var for value in self._literals for var in value.input_columns()]

    def emit_columns(self):
        return []


class FloatLiteral(EvalNode):
    def __init__(self):
        super().__init__(rule='literal', ctx='FloatLiteralContext')
        self._float_literal = None

    def parser(self, current_node: int, dag: DAG):
        children = dag.children(current_node)
        if len(children) != 1:
            raise Exception('Expected Float or Number')

        child_id_0 = children[0]

        self._float_literal = float(dag.attr(child_id_0)['value'])

        return self

    def input_columns(self):
        return []

    def emit_columns(self):
        return []


class StringLiteral(EvalNode):
    def __init__(self):
        super().__init__(rule='literal', ctx='StringLiteralContext')
        self._literal = None

    def parser(self, current_node: int, dag: DAG):
        children = dag.children(current_node)
        if len(children) != 1:
            raise Exception('Expected String literal')

        child_id_0 = children[0]

        self._literal = dag.attr(child_id_0)['value'][1:-1]

        return self

    def input_columns(self):
        return []

    def emit_columns(self):
        return []
