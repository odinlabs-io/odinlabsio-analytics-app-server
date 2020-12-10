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

import abc
from collections import defaultdict
from typing import Type, Union, Any, List, Dict


class DAG:
    def __init__(self, adj, attributes):
        self._adj = adj
        self._attributes = attributes

    def ctx(self, node_id: int):
        return self._attributes[node_id]['ctx']

    def children(self, node_id: int):
        return self._adj.get(node_id)

    def attr(self, node_id: int):
        return self._attributes.get(node_id)

    def __repr__(self):
        return str(self._adj) + str(self._attributes)


class Solver(abc.ABC):
    @abc.abstractmethod
    def solve_for_variable(self, value: Union[Any, List[Any]]) -> Union[Any, List[Any]]:
        pass


class IdentitySolver(Solver):
    def solve_for_variable(self, value: Union[Any, List[Any]]) -> Union[Any, List[Any]]:
        return value


class EvalAlternative(abc.ABC):
    def __init__(self):
        super().__init__()
        self._next = None
        self._factory = None
        self._solvers = None

    @property
    def next(self):
        return self._next() if self._next else None

    @next.setter
    def next(self, value):
        self._next = value

    @next.deleter
    def next(self):
        del self._next

    @property
    def factory(self):
        return self._factory

    @factory.setter
    def factory(self, value):
        self._factory = value

    @factory.deleter
    def factory(self):
        del self._factory

    @property
    def solvers(self):
        return self._solvers

    @solvers.setter
    def solvers(self, value):
        self._solvers = value

    @solvers.deleter
    def solvers(self):
        del self._solvers


class AlternativeBuilder:
    def __init__(self, cls: Type[EvalAlternative], solvers: Dict[str, Solver], alternative_builder, factory):
        self._cls = cls
        self._solvers = solvers
        self._alternative_builder = alternative_builder
        self._factory = factory

    def __call__(self, *args, **kwargs):
        eval_ctx = self._cls()
        eval_ctx.solvers = self._solvers

        eval_ctx.next = self._alternative_builder
        eval_ctx.factory = self._factory

        return eval_ctx


class EvalNodeFactory:
    def __init__(self):
        self._rules = dict()
        self._solvers = defaultdict(IdentitySolver)

    def evaluator(self, rule: str):
        evaluator = self._rules.get(rule)
        if not evaluator:
            raise Exception('No evaluator defined for rule {}'.format(rule))

        return self._rules.get(rule)()

    def add_evaluator(self, rule: str, cls: Type[EvalAlternative]):
        current_node = self._rules.get(rule)

        self._rules[rule] = AlternativeBuilder(cls, self._solvers, current_node, self)

    def add_solver(self, variable: str, solver: Solver):
        self._solvers[variable] = solver


class EvalNode(EvalAlternative):
    def __init__(self, rule: str, ctx: str):
        super().__init__()
        self._rule = rule
        self._ctx = ctx

    @property
    def rule(self):
        return self._rule

    @property
    def ctx(self):
        return self._ctx

    @abc.abstractmethod
    def parser(self, current_node: int, dag: DAG):
        pass

    @abc.abstractmethod
    def input_columns(self):
        return []

    @abc.abstractmethod
    def emit_columns(self):
        return []

    def build(self, current_node: int, dag: DAG):
        ctx = dag.ctx(current_node)
        if self._ctx == ctx:
            return self.parser(current_node, dag)
        else:
            next_in_rule = self.next
            if next_in_rule:
                return next_in_rule.build(current_node, dag)
            else:
                raise Exception('Reached end of rule {}. No Alternative found'.format(self._rule))
