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

# This class defines a complete listener for a parse tree produced by AggregationParser.
class AggregationListener(ParseTreeListener):

    # Enter a parse tree produced by AggregationParser#aggregationStatement.
    def enterAggregationStatement(self, ctx:AggregationParser.AggregationStatementContext):
        pass

    # Exit a parse tree produced by AggregationParser#aggregationStatement.
    def exitAggregationStatement(self, ctx:AggregationParser.AggregationStatementContext):
        pass


    # Enter a parse tree produced by AggregationParser#Reduction.
    def enterReduction(self, ctx:AggregationParser.ReductionContext):
        pass

    # Exit a parse tree produced by AggregationParser#Reduction.
    def exitReduction(self, ctx:AggregationParser.ReductionContext):
        pass


    # Enter a parse tree produced by AggregationParser#CumReduction.
    def enterCumReduction(self, ctx:AggregationParser.CumReductionContext):
        pass

    # Exit a parse tree produced by AggregationParser#CumReduction.
    def exitCumReduction(self, ctx:AggregationParser.CumReductionContext):
        pass


    # Enter a parse tree produced by AggregationParser#IdentityAggregation.
    def enterIdentityAggregation(self, ctx:AggregationParser.IdentityAggregationContext):
        pass

    # Exit a parse tree produced by AggregationParser#IdentityAggregation.
    def exitIdentityAggregation(self, ctx:AggregationParser.IdentityAggregationContext):
        pass


    # Enter a parse tree produced by AggregationParser#AggregationGroup.
    def enterAggregationGroup(self, ctx:AggregationParser.AggregationGroupContext):
        pass

    # Exit a parse tree produced by AggregationParser#AggregationGroup.
    def exitAggregationGroup(self, ctx:AggregationParser.AggregationGroupContext):
        pass


    # Enter a parse tree produced by AggregationParser#AggregationBinOp.
    def enterAggregationBinOp(self, ctx:AggregationParser.AggregationBinOpContext):
        pass

    # Exit a parse tree produced by AggregationParser#AggregationBinOp.
    def exitAggregationBinOp(self, ctx:AggregationParser.AggregationBinOpContext):
        pass


    # Enter a parse tree produced by AggregationParser#RolReduction.
    def enterRolReduction(self, ctx:AggregationParser.RolReductionContext):
        pass

    # Exit a parse tree produced by AggregationParser#RolReduction.
    def exitRolReduction(self, ctx:AggregationParser.RolReductionContext):
        pass


    # Enter a parse tree produced by AggregationParser#Count.
    def enterCount(self, ctx:AggregationParser.CountContext):
        pass

    # Exit a parse tree produced by AggregationParser#Count.
    def exitCount(self, ctx:AggregationParser.CountContext):
        pass


    # Enter a parse tree produced by AggregationParser#ExpressionGroup.
    def enterExpressionGroup(self, ctx:AggregationParser.ExpressionGroupContext):
        pass

    # Exit a parse tree produced by AggregationParser#ExpressionGroup.
    def exitExpressionGroup(self, ctx:AggregationParser.ExpressionGroupContext):
        pass


    # Enter a parse tree produced by AggregationParser#ExpressionBinOp.
    def enterExpressionBinOp(self, ctx:AggregationParser.ExpressionBinOpContext):
        pass

    # Exit a parse tree produced by AggregationParser#ExpressionBinOp.
    def exitExpressionBinOp(self, ctx:AggregationParser.ExpressionBinOpContext):
        pass


    # Enter a parse tree produced by AggregationParser#IdentityExpression.
    def enterIdentityExpression(self, ctx:AggregationParser.IdentityExpressionContext):
        pass

    # Exit a parse tree produced by AggregationParser#IdentityExpression.
    def exitIdentityExpression(self, ctx:AggregationParser.IdentityExpressionContext):
        pass


    # Enter a parse tree produced by AggregationParser#conditionStatement.
    def enterConditionStatement(self, ctx:AggregationParser.ConditionStatementContext):
        pass

    # Exit a parse tree produced by AggregationParser#conditionStatement.
    def exitConditionStatement(self, ctx:AggregationParser.ConditionStatementContext):
        pass


    # Enter a parse tree produced by AggregationParser#ConditionBinOp.
    def enterConditionBinOp(self, ctx:AggregationParser.ConditionBinOpContext):
        pass

    # Exit a parse tree produced by AggregationParser#ConditionBinOp.
    def exitConditionBinOp(self, ctx:AggregationParser.ConditionBinOpContext):
        pass


    # Enter a parse tree produced by AggregationParser#ConditionNegate.
    def enterConditionNegate(self, ctx:AggregationParser.ConditionNegateContext):
        pass

    # Exit a parse tree produced by AggregationParser#ConditionNegate.
    def exitConditionNegate(self, ctx:AggregationParser.ConditionNegateContext):
        pass


    # Enter a parse tree produced by AggregationParser#IdentityCondition.
    def enterIdentityCondition(self, ctx:AggregationParser.IdentityConditionContext):
        pass

    # Exit a parse tree produced by AggregationParser#IdentityCondition.
    def exitIdentityCondition(self, ctx:AggregationParser.IdentityConditionContext):
        pass


    # Enter a parse tree produced by AggregationParser#ConditionGroup.
    def enterConditionGroup(self, ctx:AggregationParser.ConditionGroupContext):
        pass

    # Exit a parse tree produced by AggregationParser#ConditionGroup.
    def exitConditionGroup(self, ctx:AggregationParser.ConditionGroupContext):
        pass


    # Enter a parse tree produced by AggregationParser#SelectorOrder.
    def enterSelectorOrder(self, ctx:AggregationParser.SelectorOrderContext):
        pass

    # Exit a parse tree produced by AggregationParser#SelectorOrder.
    def exitSelectorOrder(self, ctx:AggregationParser.SelectorOrderContext):
        pass


    # Enter a parse tree produced by AggregationParser#SelectorIn.
    def enterSelectorIn(self, ctx:AggregationParser.SelectorInContext):
        pass

    # Exit a parse tree produced by AggregationParser#SelectorIn.
    def exitSelectorIn(self, ctx:AggregationParser.SelectorInContext):
        pass


    # Enter a parse tree produced by AggregationParser#ConstantMeasure.
    def enterConstantMeasure(self, ctx:AggregationParser.ConstantMeasureContext):
        pass

    # Exit a parse tree produced by AggregationParser#ConstantMeasure.
    def exitConstantMeasure(self, ctx:AggregationParser.ConstantMeasureContext):
        pass


    # Enter a parse tree produced by AggregationParser#ReferenceMeasure.
    def enterReferenceMeasure(self, ctx:AggregationParser.ReferenceMeasureContext):
        pass

    # Exit a parse tree produced by AggregationParser#ReferenceMeasure.
    def exitReferenceMeasure(self, ctx:AggregationParser.ReferenceMeasureContext):
        pass


    # Enter a parse tree produced by AggregationParser#ReferenceCategory.
    def enterReferenceCategory(self, ctx:AggregationParser.ReferenceCategoryContext):
        pass

    # Exit a parse tree produced by AggregationParser#ReferenceCategory.
    def exitReferenceCategory(self, ctx:AggregationParser.ReferenceCategoryContext):
        pass


    # Enter a parse tree produced by AggregationParser#literals.
    def enterLiterals(self, ctx:AggregationParser.LiteralsContext):
        pass

    # Exit a parse tree produced by AggregationParser#literals.
    def exitLiterals(self, ctx:AggregationParser.LiteralsContext):
        pass


    # Enter a parse tree produced by AggregationParser#FloatLiteral.
    def enterFloatLiteral(self, ctx:AggregationParser.FloatLiteralContext):
        pass

    # Exit a parse tree produced by AggregationParser#FloatLiteral.
    def exitFloatLiteral(self, ctx:AggregationParser.FloatLiteralContext):
        pass


    # Enter a parse tree produced by AggregationParser#StringLiteral.
    def enterStringLiteral(self, ctx:AggregationParser.StringLiteralContext):
        pass

    # Exit a parse tree produced by AggregationParser#StringLiteral.
    def exitStringLiteral(self, ctx:AggregationParser.StringLiteralContext):
        pass



del AggregationParser