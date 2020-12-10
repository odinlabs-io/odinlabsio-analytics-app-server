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

from collections import defaultdict

from antlr4 import CommonTokenStream, InputStream, ParseTreeVisitor, TerminalNode

from app.aggregation.dag import DAG
from app.aggregation.parser.gen.AggregationLexer import AggregationLexer
from app.aggregation.parser.gen.AggregationParser import AggregationParser


class Visitor(ParseTreeVisitor):
    def __init__(self):
        super().__init__()

    def visitChildren(self, node) -> DAG:
        adj = defaultdict(list)
        attributes = dict()
        count = 0
        nodes = list([{'id': count, 'node': node}])

        current = nodes.pop()
        while current:
            current_id = current['id']
            current_node = current['node']
            if isinstance(current_node, TerminalNode):
                attributes[current_id] = {'id': current_id, 'value': current_node.getText(),
                                          'symbol': current_node.getSymbol().type, 'type': 'Symbol'}
            elif current_node.exception:
                raise Exception("Invalid Statement Input")
            else:
                if current_node.children and len(current_node.children) > 0:
                    children = current_node.children
                    n = len(children)
                    for i in range(n):
                        child_node = children[i]
                        child_id = count + i + 1
                        nodes.append({'id': child_id, 'node': child_node})
                        adj[current_id].append(child_id)
                    count = count + n
                attributes[current_id] = {'id': current_id, 'value': current_node.getText(),
                                          'type': 'ctx', 'ctx': type(current_node).__name__}
            if len(nodes) > 0:
                current = nodes.pop()
            else:
                break

        return DAG(adj, attributes)


def aggregation_dag(input: str) -> DAG:
    stream = CommonTokenStream(AggregationLexer(InputStream(input)))
    return AggregationParser(stream).aggregationStatement().accept(Visitor())


def filter_dag(input: str) -> DAG:
    stream = CommonTokenStream(AggregationLexer(InputStream(input)))
    return AggregationParser(stream).conditionStatement().accept(Visitor())
