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

# Generated from Aggregation.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .AggregationParser import AggregationParser
else:
    from AggregationParser import AggregationParser

# This class defines a complete generic visitor for a parse tree produced by AggregationParser.

class AggregationVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by AggregationParser#aggregationStatement.
    def visitAggregationStatement(self, ctx:AggregationParser.AggregationStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AggregationParser#Reduction.
    def visitReduction(self, ctx:AggregationParser.ReductionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AggregationParser#CumReduction.
    def visitCumReduction(self, ctx:AggregationParser.CumReductionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AggregationParser#IdentityAggregation.
    def visitIdentityAggregation(self, ctx:AggregationParser.IdentityAggregationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AggregationParser#AggregationGroup.
    def visitAggregationGroup(self, ctx:AggregationParser.AggregationGroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AggregationParser#AggregationBinOp.
    def visitAggregationBinOp(self, ctx:AggregationParser.AggregationBinOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AggregationParser#RolReduction.
    def visitRolReduction(self, ctx:AggregationParser.RolReductionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AggregationParser#Count.
    def visitCount(self, ctx:AggregationParser.CountContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AggregationParser#ExpressionGroup.
    def visitExpressionGroup(self, ctx:AggregationParser.ExpressionGroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AggregationParser#ExpressionBinOp.
    def visitExpressionBinOp(self, ctx:AggregationParser.ExpressionBinOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AggregationParser#IdentityExpression.
    def visitIdentityExpression(self, ctx:AggregationParser.IdentityExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AggregationParser#conditionStatement.
    def visitConditionStatement(self, ctx:AggregationParser.ConditionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AggregationParser#ConditionBinOp.
    def visitConditionBinOp(self, ctx:AggregationParser.ConditionBinOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AggregationParser#ConditionNegate.
    def visitConditionNegate(self, ctx:AggregationParser.ConditionNegateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AggregationParser#IdentityCondition.
    def visitIdentityCondition(self, ctx:AggregationParser.IdentityConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AggregationParser#ConditionGroup.
    def visitConditionGroup(self, ctx:AggregationParser.ConditionGroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AggregationParser#SelectorOrder.
    def visitSelectorOrder(self, ctx:AggregationParser.SelectorOrderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AggregationParser#SelectorIn.
    def visitSelectorIn(self, ctx:AggregationParser.SelectorInContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AggregationParser#ConstantMeasure.
    def visitConstantMeasure(self, ctx:AggregationParser.ConstantMeasureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AggregationParser#ReferenceMeasure.
    def visitReferenceMeasure(self, ctx:AggregationParser.ReferenceMeasureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AggregationParser#ReferenceCategory.
    def visitReferenceCategory(self, ctx:AggregationParser.ReferenceCategoryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AggregationParser#literals.
    def visitLiterals(self, ctx:AggregationParser.LiteralsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AggregationParser#FloatLiteral.
    def visitFloatLiteral(self, ctx:AggregationParser.FloatLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AggregationParser#StringLiteral.
    def visitStringLiteral(self, ctx:AggregationParser.StringLiteralContext):
        return self.visitChildren(ctx)



del AggregationParser