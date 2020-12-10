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
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\26")
        buf.write("\u00af\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\2\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3$\n\3\f\3\16\3\'\13")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3\60\n\3\f\3\16\3\63")
        buf.write("\13\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3?\n\3")
        buf.write("\f\3\16\3B\13\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\7\3P\n\3\f\3\16\3S\13\3\3\3\3\3\3\3\5\3X\n")
        buf.write("\3\3\3\3\3\3\3\7\3]\n\3\f\3\16\3`\13\3\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\5\4h\n\4\3\4\3\4\3\4\7\4m\n\4\f\4\16\4p\13\4")
        buf.write("\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\5\6\u0080\n\6\3\6\3\6\3\6\7\6\u0085\n\6\f\6\16\6\u0088")
        buf.write("\13\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\5\7\u0098\n\7\3\b\3\b\5\b\u009c\n\b\3\t\3\t\3")
        buf.write("\n\3\n\3\n\3\n\7\n\u00a4\n\n\f\n\16\n\u00a7\13\n\3\n\3")
        buf.write("\n\3\13\3\13\5\13\u00ad\n\13\3\13\2\5\4\6\n\f\2\4\6\b")
        buf.write("\n\f\16\20\22\24\2\3\3\2\3\4\2\u00b7\2\26\3\2\2\2\4W\3")
        buf.write("\2\2\2\6g\3\2\2\2\bq\3\2\2\2\n\177\3\2\2\2\f\u0097\3\2")
        buf.write("\2\2\16\u009b\3\2\2\2\20\u009d\3\2\2\2\22\u009f\3\2\2")
        buf.write("\2\24\u00ac\3\2\2\2\26\27\5\4\3\2\27\30\7\2\2\3\30\3\3")
        buf.write("\2\2\2\31\32\b\3\1\2\32\33\7\17\2\2\33\34\5\4\3\2\34\35")
        buf.write("\7\20\2\2\35X\3\2\2\2\36\37\7\6\2\2\37 \7\17\2\2 %\5\6")
        buf.write("\4\2!\"\7\23\2\2\"$\5\n\6\2#!\3\2\2\2$\'\3\2\2\2%#\3\2")
        buf.write("\2\2%&\3\2\2\2&(\3\2\2\2\'%\3\2\2\2()\7\20\2\2)X\3\2\2")
        buf.write("\2*+\7\t\2\2+,\7\17\2\2,\61\5\20\t\2-.\7\23\2\2.\60\5")
        buf.write("\n\6\2/-\3\2\2\2\60\63\3\2\2\2\61/\3\2\2\2\61\62\3\2\2")
        buf.write("\2\62\64\3\2\2\2\63\61\3\2\2\2\64\65\7\20\2\2\65X\3\2")
        buf.write("\2\2\66\67\7\7\2\2\678\7\17\2\289\7\5\2\29:\7\24\2\2:")
        buf.write(";\7\23\2\2;@\5\6\4\2<=\7\23\2\2=?\5\n\6\2><\3\2\2\2?B")
        buf.write("\3\2\2\2@>\3\2\2\2@A\3\2\2\2AC\3\2\2\2B@\3\2\2\2CD\7\20")
        buf.write("\2\2DX\3\2\2\2EF\7\b\2\2FG\7\17\2\2GH\7\3\2\2HI\7\23\2")
        buf.write("\2IJ\7\5\2\2JK\7\24\2\2KL\7\23\2\2LQ\5\6\4\2MN\7\23\2")
        buf.write("\2NP\5\n\6\2OM\3\2\2\2PS\3\2\2\2QO\3\2\2\2QR\3\2\2\2R")
        buf.write("T\3\2\2\2SQ\3\2\2\2TU\7\20\2\2UX\3\2\2\2VX\5\6\4\2W\31")
        buf.write("\3\2\2\2W\36\3\2\2\2W*\3\2\2\2W\66\3\2\2\2WE\3\2\2\2W")
        buf.write("V\3\2\2\2X^\3\2\2\2YZ\f\t\2\2Z[\7\16\2\2[]\5\4\3\n\\Y")
        buf.write("\3\2\2\2]`\3\2\2\2^\\\3\2\2\2^_\3\2\2\2_\5\3\2\2\2`^\3")
        buf.write("\2\2\2ab\b\4\1\2bc\7\17\2\2cd\5\6\4\2de\7\20\2\2eh\3\2")
        buf.write("\2\2fh\5\16\b\2ga\3\2\2\2gf\3\2\2\2hn\3\2\2\2ij\f\5\2")
        buf.write("\2jk\7\16\2\2km\5\6\4\6li\3\2\2\2mp\3\2\2\2nl\3\2\2\2")
        buf.write("no\3\2\2\2o\7\3\2\2\2pn\3\2\2\2qr\5\n\6\2rs\7\2\2\3s\t")
        buf.write("\3\2\2\2tu\b\6\1\2uv\7\17\2\2vw\5\n\6\2wx\7\20\2\2x\u0080")
        buf.write("\3\2\2\2yz\7\f\2\2z{\7\17\2\2{|\5\n\6\2|}\7\20\2\2}\u0080")
        buf.write("\3\2\2\2~\u0080\5\f\7\2\177t\3\2\2\2\177y\3\2\2\2\177")
        buf.write("~\3\2\2\2\u0080\u0086\3\2\2\2\u0081\u0082\f\6\2\2\u0082")
        buf.write("\u0083\7\r\2\2\u0083\u0085\5\n\6\7\u0084\u0081\3\2\2\2")
        buf.write("\u0085\u0088\3\2\2\2\u0086\u0084\3\2\2\2\u0086\u0087\3")
        buf.write("\2\2\2\u0087\13\3\2\2\2\u0088\u0086\3\2\2\2\u0089\u008a")
        buf.write("\7\n\2\2\u008a\u008b\7\17\2\2\u008b\u008c\5\20\t\2\u008c")
        buf.write("\u008d\7\23\2\2\u008d\u008e\5\24\13\2\u008e\u008f\7\20")
        buf.write("\2\2\u008f\u0098\3\2\2\2\u0090\u0091\7\13\2\2\u0091\u0092")
        buf.write("\7\17\2\2\u0092\u0093\5\20\t\2\u0093\u0094\7\23\2\2\u0094")
        buf.write("\u0095\5\22\n\2\u0095\u0096\7\20\2\2\u0096\u0098\3\2\2")
        buf.write("\2\u0097\u0089\3\2\2\2\u0097\u0090\3\2\2\2\u0098\r\3\2")
        buf.write("\2\2\u0099\u009c\t\2\2\2\u009a\u009c\7\24\2\2\u009b\u0099")
        buf.write("\3\2\2\2\u009b\u009a\3\2\2\2\u009c\17\3\2\2\2\u009d\u009e")
        buf.write("\7\24\2\2\u009e\21\3\2\2\2\u009f\u00a0\7\21\2\2\u00a0")
        buf.write("\u00a5\5\24\13\2\u00a1\u00a2\7\23\2\2\u00a2\u00a4\5\24")
        buf.write("\13\2\u00a3\u00a1\3\2\2\2\u00a4\u00a7\3\2\2\2\u00a5\u00a3")
        buf.write("\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a6\u00a8\3\2\2\2\u00a7")
        buf.write("\u00a5\3\2\2\2\u00a8\u00a9\7\22\2\2\u00a9\23\3\2\2\2\u00aa")
        buf.write("\u00ad\t\2\2\2\u00ab\u00ad\7\25\2\2\u00ac\u00aa\3\2\2")
        buf.write("\2\u00ac\u00ab\3\2\2\2\u00ad\25\3\2\2\2\20%\61@QW^gn\177")
        buf.write("\u0086\u0097\u009b\u00a5\u00ac")
        return buf.getvalue()


class AggregationParser ( Parser ):

    grammarFileName = "Aggregation.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'IN'", "'NOT'", "<INVALID>", "<INVALID>", 
                     "'('", "')'", "'['", "']'", "','" ]

    symbolicNames = [ "<INVALID>", "NUMBER", "FLOAT", "SORT", "AGGR", "CUMAGGR", 
                      "ROLAGGR", "COUNT", "ORDEROPERATOR", "IN", "NOT", 
                      "SETOPERATOR", "ARITHMOPERATOR", "LPAREN", "RPAREN", 
                      "LBRACK", "RBRACK", "COMMA", "ID_LITERAL", "STR_LITERAL", 
                      "WS" ]

    RULE_aggregationStatement = 0
    RULE_aggregation = 1
    RULE_expression = 2
    RULE_conditionStatement = 3
    RULE_condition = 4
    RULE_selector = 5
    RULE_measure = 6
    RULE_category = 7
    RULE_literals = 8
    RULE_literal = 9

    ruleNames =  [ "aggregationStatement", "aggregation", "expression", 
                   "conditionStatement", "condition", "selector", "measure", 
                   "category", "literals", "literal" ]

    EOF = Token.EOF
    NUMBER=1
    FLOAT=2
    SORT=3
    AGGR=4
    CUMAGGR=5
    ROLAGGR=6
    COUNT=7
    ORDEROPERATOR=8
    IN=9
    NOT=10
    SETOPERATOR=11
    ARITHMOPERATOR=12
    LPAREN=13
    RPAREN=14
    LBRACK=15
    RBRACK=16
    COMMA=17
    ID_LITERAL=18
    STR_LITERAL=19
    WS=20

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class AggregationStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def aggregation(self):
            return self.getTypedRuleContext(AggregationParser.AggregationContext,0)


        def EOF(self):
            return self.getToken(AggregationParser.EOF, 0)

        def getRuleIndex(self):
            return AggregationParser.RULE_aggregationStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAggregationStatement" ):
                listener.enterAggregationStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAggregationStatement" ):
                listener.exitAggregationStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAggregationStatement" ):
                return visitor.visitAggregationStatement(self)
            else:
                return visitor.visitChildren(self)




    def aggregationStatement(self):

        localctx = AggregationParser.AggregationStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_aggregationStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.aggregation(0)
            self.state = 21
            self.match(AggregationParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AggregationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AggregationParser.RULE_aggregation

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ReductionContext(AggregationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AggregationParser.AggregationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def AGGR(self):
            return self.getToken(AggregationParser.AGGR, 0)
        def LPAREN(self):
            return self.getToken(AggregationParser.LPAREN, 0)
        def expression(self):
            return self.getTypedRuleContext(AggregationParser.ExpressionContext,0)

        def RPAREN(self):
            return self.getToken(AggregationParser.RPAREN, 0)
        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(AggregationParser.COMMA)
            else:
                return self.getToken(AggregationParser.COMMA, i)
        def condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AggregationParser.ConditionContext)
            else:
                return self.getTypedRuleContext(AggregationParser.ConditionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReduction" ):
                listener.enterReduction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReduction" ):
                listener.exitReduction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReduction" ):
                return visitor.visitReduction(self)
            else:
                return visitor.visitChildren(self)


    class CumReductionContext(AggregationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AggregationParser.AggregationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CUMAGGR(self):
            return self.getToken(AggregationParser.CUMAGGR, 0)
        def LPAREN(self):
            return self.getToken(AggregationParser.LPAREN, 0)
        def SORT(self):
            return self.getToken(AggregationParser.SORT, 0)
        def ID_LITERAL(self):
            return self.getToken(AggregationParser.ID_LITERAL, 0)
        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(AggregationParser.COMMA)
            else:
                return self.getToken(AggregationParser.COMMA, i)
        def expression(self):
            return self.getTypedRuleContext(AggregationParser.ExpressionContext,0)

        def RPAREN(self):
            return self.getToken(AggregationParser.RPAREN, 0)
        def condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AggregationParser.ConditionContext)
            else:
                return self.getTypedRuleContext(AggregationParser.ConditionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCumReduction" ):
                listener.enterCumReduction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCumReduction" ):
                listener.exitCumReduction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCumReduction" ):
                return visitor.visitCumReduction(self)
            else:
                return visitor.visitChildren(self)


    class IdentityAggregationContext(AggregationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AggregationParser.AggregationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(AggregationParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentityAggregation" ):
                listener.enterIdentityAggregation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentityAggregation" ):
                listener.exitIdentityAggregation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentityAggregation" ):
                return visitor.visitIdentityAggregation(self)
            else:
                return visitor.visitChildren(self)


    class AggregationGroupContext(AggregationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AggregationParser.AggregationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(AggregationParser.LPAREN, 0)
        def aggregation(self):
            return self.getTypedRuleContext(AggregationParser.AggregationContext,0)

        def RPAREN(self):
            return self.getToken(AggregationParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAggregationGroup" ):
                listener.enterAggregationGroup(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAggregationGroup" ):
                listener.exitAggregationGroup(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAggregationGroup" ):
                return visitor.visitAggregationGroup(self)
            else:
                return visitor.visitChildren(self)


    class AggregationBinOpContext(AggregationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AggregationParser.AggregationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def aggregation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AggregationParser.AggregationContext)
            else:
                return self.getTypedRuleContext(AggregationParser.AggregationContext,i)

        def ARITHMOPERATOR(self):
            return self.getToken(AggregationParser.ARITHMOPERATOR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAggregationBinOp" ):
                listener.enterAggregationBinOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAggregationBinOp" ):
                listener.exitAggregationBinOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAggregationBinOp" ):
                return visitor.visitAggregationBinOp(self)
            else:
                return visitor.visitChildren(self)


    class RolReductionContext(AggregationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AggregationParser.AggregationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ROLAGGR(self):
            return self.getToken(AggregationParser.ROLAGGR, 0)
        def LPAREN(self):
            return self.getToken(AggregationParser.LPAREN, 0)
        def NUMBER(self):
            return self.getToken(AggregationParser.NUMBER, 0)
        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(AggregationParser.COMMA)
            else:
                return self.getToken(AggregationParser.COMMA, i)
        def SORT(self):
            return self.getToken(AggregationParser.SORT, 0)
        def ID_LITERAL(self):
            return self.getToken(AggregationParser.ID_LITERAL, 0)
        def expression(self):
            return self.getTypedRuleContext(AggregationParser.ExpressionContext,0)

        def RPAREN(self):
            return self.getToken(AggregationParser.RPAREN, 0)
        def condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AggregationParser.ConditionContext)
            else:
                return self.getTypedRuleContext(AggregationParser.ConditionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRolReduction" ):
                listener.enterRolReduction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRolReduction" ):
                listener.exitRolReduction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRolReduction" ):
                return visitor.visitRolReduction(self)
            else:
                return visitor.visitChildren(self)


    class CountContext(AggregationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AggregationParser.AggregationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def COUNT(self):
            return self.getToken(AggregationParser.COUNT, 0)
        def LPAREN(self):
            return self.getToken(AggregationParser.LPAREN, 0)
        def category(self):
            return self.getTypedRuleContext(AggregationParser.CategoryContext,0)

        def RPAREN(self):
            return self.getToken(AggregationParser.RPAREN, 0)
        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(AggregationParser.COMMA)
            else:
                return self.getToken(AggregationParser.COMMA, i)
        def condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AggregationParser.ConditionContext)
            else:
                return self.getTypedRuleContext(AggregationParser.ConditionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCount" ):
                listener.enterCount(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCount" ):
                listener.exitCount(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCount" ):
                return visitor.visitCount(self)
            else:
                return visitor.visitChildren(self)



    def aggregation(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = AggregationParser.AggregationContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_aggregation, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = AggregationParser.AggregationGroupContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 24
                self.match(AggregationParser.LPAREN)
                self.state = 25
                self.aggregation(0)
                self.state = 26
                self.match(AggregationParser.RPAREN)
                pass

            elif la_ == 2:
                localctx = AggregationParser.ReductionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 28
                self.match(AggregationParser.AGGR)
                self.state = 29
                self.match(AggregationParser.LPAREN)
                self.state = 30
                self.expression(0)
                self.state = 35
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==AggregationParser.COMMA:
                    self.state = 31
                    self.match(AggregationParser.COMMA)
                    self.state = 32
                    self.condition(0)
                    self.state = 37
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 38
                self.match(AggregationParser.RPAREN)
                pass

            elif la_ == 3:
                localctx = AggregationParser.CountContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 40
                self.match(AggregationParser.COUNT)
                self.state = 41
                self.match(AggregationParser.LPAREN)
                self.state = 42
                self.category()
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==AggregationParser.COMMA:
                    self.state = 43
                    self.match(AggregationParser.COMMA)
                    self.state = 44
                    self.condition(0)
                    self.state = 49
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 50
                self.match(AggregationParser.RPAREN)
                pass

            elif la_ == 4:
                localctx = AggregationParser.CumReductionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 52
                self.match(AggregationParser.CUMAGGR)
                self.state = 53
                self.match(AggregationParser.LPAREN)
                self.state = 54
                self.match(AggregationParser.SORT)
                self.state = 55
                self.match(AggregationParser.ID_LITERAL)
                self.state = 56
                self.match(AggregationParser.COMMA)
                self.state = 57
                self.expression(0)
                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==AggregationParser.COMMA:
                    self.state = 58
                    self.match(AggregationParser.COMMA)
                    self.state = 59
                    self.condition(0)
                    self.state = 64
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 65
                self.match(AggregationParser.RPAREN)
                pass

            elif la_ == 5:
                localctx = AggregationParser.RolReductionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 67
                self.match(AggregationParser.ROLAGGR)
                self.state = 68
                self.match(AggregationParser.LPAREN)
                self.state = 69
                self.match(AggregationParser.NUMBER)
                self.state = 70
                self.match(AggregationParser.COMMA)
                self.state = 71
                self.match(AggregationParser.SORT)
                self.state = 72
                self.match(AggregationParser.ID_LITERAL)
                self.state = 73
                self.match(AggregationParser.COMMA)
                self.state = 74
                self.expression(0)
                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==AggregationParser.COMMA:
                    self.state = 75
                    self.match(AggregationParser.COMMA)
                    self.state = 76
                    self.condition(0)
                    self.state = 81
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 82
                self.match(AggregationParser.RPAREN)
                pass

            elif la_ == 6:
                localctx = AggregationParser.IdentityAggregationContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 84
                self.expression(0)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 92
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = AggregationParser.AggregationBinOpContext(self, AggregationParser.AggregationContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_aggregation)
                    self.state = 87
                    if not self.precpred(self._ctx, 7):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                    self.state = 88
                    self.match(AggregationParser.ARITHMOPERATOR)
                    self.state = 89
                    self.aggregation(8) 
                self.state = 94
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AggregationParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ExpressionGroupContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AggregationParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(AggregationParser.LPAREN, 0)
        def expression(self):
            return self.getTypedRuleContext(AggregationParser.ExpressionContext,0)

        def RPAREN(self):
            return self.getToken(AggregationParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionGroup" ):
                listener.enterExpressionGroup(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionGroup" ):
                listener.exitExpressionGroup(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionGroup" ):
                return visitor.visitExpressionGroup(self)
            else:
                return visitor.visitChildren(self)


    class ExpressionBinOpContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AggregationParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AggregationParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(AggregationParser.ExpressionContext,i)

        def ARITHMOPERATOR(self):
            return self.getToken(AggregationParser.ARITHMOPERATOR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionBinOp" ):
                listener.enterExpressionBinOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionBinOp" ):
                listener.exitExpressionBinOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionBinOp" ):
                return visitor.visitExpressionBinOp(self)
            else:
                return visitor.visitChildren(self)


    class IdentityExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AggregationParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def measure(self):
            return self.getTypedRuleContext(AggregationParser.MeasureContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentityExpression" ):
                listener.enterIdentityExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentityExpression" ):
                listener.exitIdentityExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentityExpression" ):
                return visitor.visitIdentityExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = AggregationParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [AggregationParser.LPAREN]:
                localctx = AggregationParser.ExpressionGroupContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 96
                self.match(AggregationParser.LPAREN)
                self.state = 97
                self.expression(0)
                self.state = 98
                self.match(AggregationParser.RPAREN)
                pass
            elif token in [AggregationParser.NUMBER, AggregationParser.FLOAT, AggregationParser.ID_LITERAL]:
                localctx = AggregationParser.IdentityExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 100
                self.measure()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 108
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = AggregationParser.ExpressionBinOpContext(self, AggregationParser.ExpressionContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 103
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 104
                    self.match(AggregationParser.ARITHMOPERATOR)
                    self.state = 105
                    self.expression(4) 
                self.state = 110
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ConditionStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self):
            return self.getTypedRuleContext(AggregationParser.ConditionContext,0)


        def EOF(self):
            return self.getToken(AggregationParser.EOF, 0)

        def getRuleIndex(self):
            return AggregationParser.RULE_conditionStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditionStatement" ):
                listener.enterConditionStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditionStatement" ):
                listener.exitConditionStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditionStatement" ):
                return visitor.visitConditionStatement(self)
            else:
                return visitor.visitChildren(self)




    def conditionStatement(self):

        localctx = AggregationParser.ConditionStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_conditionStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.condition(0)
            self.state = 112
            self.match(AggregationParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AggregationParser.RULE_condition

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ConditionBinOpContext(ConditionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AggregationParser.ConditionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AggregationParser.ConditionContext)
            else:
                return self.getTypedRuleContext(AggregationParser.ConditionContext,i)

        def SETOPERATOR(self):
            return self.getToken(AggregationParser.SETOPERATOR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditionBinOp" ):
                listener.enterConditionBinOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditionBinOp" ):
                listener.exitConditionBinOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditionBinOp" ):
                return visitor.visitConditionBinOp(self)
            else:
                return visitor.visitChildren(self)


    class ConditionNegateContext(ConditionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AggregationParser.ConditionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(AggregationParser.NOT, 0)
        def LPAREN(self):
            return self.getToken(AggregationParser.LPAREN, 0)
        def condition(self):
            return self.getTypedRuleContext(AggregationParser.ConditionContext,0)

        def RPAREN(self):
            return self.getToken(AggregationParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditionNegate" ):
                listener.enterConditionNegate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditionNegate" ):
                listener.exitConditionNegate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditionNegate" ):
                return visitor.visitConditionNegate(self)
            else:
                return visitor.visitChildren(self)


    class IdentityConditionContext(ConditionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AggregationParser.ConditionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def selector(self):
            return self.getTypedRuleContext(AggregationParser.SelectorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentityCondition" ):
                listener.enterIdentityCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentityCondition" ):
                listener.exitIdentityCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentityCondition" ):
                return visitor.visitIdentityCondition(self)
            else:
                return visitor.visitChildren(self)


    class ConditionGroupContext(ConditionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AggregationParser.ConditionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(AggregationParser.LPAREN, 0)
        def condition(self):
            return self.getTypedRuleContext(AggregationParser.ConditionContext,0)

        def RPAREN(self):
            return self.getToken(AggregationParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditionGroup" ):
                listener.enterConditionGroup(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditionGroup" ):
                listener.exitConditionGroup(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditionGroup" ):
                return visitor.visitConditionGroup(self)
            else:
                return visitor.visitChildren(self)



    def condition(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = AggregationParser.ConditionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_condition, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [AggregationParser.LPAREN]:
                localctx = AggregationParser.ConditionGroupContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 115
                self.match(AggregationParser.LPAREN)
                self.state = 116
                self.condition(0)
                self.state = 117
                self.match(AggregationParser.RPAREN)
                pass
            elif token in [AggregationParser.NOT]:
                localctx = AggregationParser.ConditionNegateContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 119
                self.match(AggregationParser.NOT)
                self.state = 120
                self.match(AggregationParser.LPAREN)
                self.state = 121
                self.condition(0)
                self.state = 122
                self.match(AggregationParser.RPAREN)
                pass
            elif token in [AggregationParser.ORDEROPERATOR, AggregationParser.IN]:
                localctx = AggregationParser.IdentityConditionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 124
                self.selector()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 132
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = AggregationParser.ConditionBinOpContext(self, AggregationParser.ConditionContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_condition)
                    self.state = 127
                    if not self.precpred(self._ctx, 4):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                    self.state = 128
                    self.match(AggregationParser.SETOPERATOR)
                    self.state = 129
                    self.condition(5) 
                self.state = 134
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class SelectorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AggregationParser.RULE_selector

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SelectorInContext(SelectorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AggregationParser.SelectorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IN(self):
            return self.getToken(AggregationParser.IN, 0)
        def LPAREN(self):
            return self.getToken(AggregationParser.LPAREN, 0)
        def category(self):
            return self.getTypedRuleContext(AggregationParser.CategoryContext,0)

        def COMMA(self):
            return self.getToken(AggregationParser.COMMA, 0)
        def literals(self):
            return self.getTypedRuleContext(AggregationParser.LiteralsContext,0)

        def RPAREN(self):
            return self.getToken(AggregationParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectorIn" ):
                listener.enterSelectorIn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectorIn" ):
                listener.exitSelectorIn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelectorIn" ):
                return visitor.visitSelectorIn(self)
            else:
                return visitor.visitChildren(self)


    class SelectorOrderContext(SelectorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AggregationParser.SelectorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ORDEROPERATOR(self):
            return self.getToken(AggregationParser.ORDEROPERATOR, 0)
        def LPAREN(self):
            return self.getToken(AggregationParser.LPAREN, 0)
        def category(self):
            return self.getTypedRuleContext(AggregationParser.CategoryContext,0)

        def COMMA(self):
            return self.getToken(AggregationParser.COMMA, 0)
        def literal(self):
            return self.getTypedRuleContext(AggregationParser.LiteralContext,0)

        def RPAREN(self):
            return self.getToken(AggregationParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectorOrder" ):
                listener.enterSelectorOrder(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectorOrder" ):
                listener.exitSelectorOrder(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelectorOrder" ):
                return visitor.visitSelectorOrder(self)
            else:
                return visitor.visitChildren(self)



    def selector(self):

        localctx = AggregationParser.SelectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_selector)
        try:
            self.state = 149
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [AggregationParser.ORDEROPERATOR]:
                localctx = AggregationParser.SelectorOrderContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                self.match(AggregationParser.ORDEROPERATOR)
                self.state = 136
                self.match(AggregationParser.LPAREN)
                self.state = 137
                self.category()
                self.state = 138
                self.match(AggregationParser.COMMA)
                self.state = 139
                self.literal()
                self.state = 140
                self.match(AggregationParser.RPAREN)
                pass
            elif token in [AggregationParser.IN]:
                localctx = AggregationParser.SelectorInContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 142
                self.match(AggregationParser.IN)
                self.state = 143
                self.match(AggregationParser.LPAREN)
                self.state = 144
                self.category()
                self.state = 145
                self.match(AggregationParser.COMMA)
                self.state = 146
                self.literals()
                self.state = 147
                self.match(AggregationParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MeasureContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AggregationParser.RULE_measure

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ReferenceMeasureContext(MeasureContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AggregationParser.MeasureContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID_LITERAL(self):
            return self.getToken(AggregationParser.ID_LITERAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReferenceMeasure" ):
                listener.enterReferenceMeasure(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReferenceMeasure" ):
                listener.exitReferenceMeasure(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReferenceMeasure" ):
                return visitor.visitReferenceMeasure(self)
            else:
                return visitor.visitChildren(self)


    class ConstantMeasureContext(MeasureContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AggregationParser.MeasureContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(AggregationParser.FLOAT, 0)
        def NUMBER(self):
            return self.getToken(AggregationParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstantMeasure" ):
                listener.enterConstantMeasure(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstantMeasure" ):
                listener.exitConstantMeasure(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstantMeasure" ):
                return visitor.visitConstantMeasure(self)
            else:
                return visitor.visitChildren(self)



    def measure(self):

        localctx = AggregationParser.MeasureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_measure)
        self._la = 0 # Token type
        try:
            self.state = 153
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [AggregationParser.NUMBER, AggregationParser.FLOAT]:
                localctx = AggregationParser.ConstantMeasureContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 151
                _la = self._input.LA(1)
                if not(_la==AggregationParser.NUMBER or _la==AggregationParser.FLOAT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [AggregationParser.ID_LITERAL]:
                localctx = AggregationParser.ReferenceMeasureContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 152
                self.match(AggregationParser.ID_LITERAL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CategoryContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AggregationParser.RULE_category

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ReferenceCategoryContext(CategoryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AggregationParser.CategoryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID_LITERAL(self):
            return self.getToken(AggregationParser.ID_LITERAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReferenceCategory" ):
                listener.enterReferenceCategory(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReferenceCategory" ):
                listener.exitReferenceCategory(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReferenceCategory" ):
                return visitor.visitReferenceCategory(self)
            else:
                return visitor.visitChildren(self)



    def category(self):

        localctx = AggregationParser.CategoryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_category)
        try:
            localctx = AggregationParser.ReferenceCategoryContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(AggregationParser.ID_LITERAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(AggregationParser.LBRACK, 0)

        def literal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AggregationParser.LiteralContext)
            else:
                return self.getTypedRuleContext(AggregationParser.LiteralContext,i)


        def RBRACK(self):
            return self.getToken(AggregationParser.RBRACK, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(AggregationParser.COMMA)
            else:
                return self.getToken(AggregationParser.COMMA, i)

        def getRuleIndex(self):
            return AggregationParser.RULE_literals

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiterals" ):
                listener.enterLiterals(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiterals" ):
                listener.exitLiterals(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiterals" ):
                return visitor.visitLiterals(self)
            else:
                return visitor.visitChildren(self)




    def literals(self):

        localctx = AggregationParser.LiteralsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_literals)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.match(AggregationParser.LBRACK)
            self.state = 158
            self.literal()
            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==AggregationParser.COMMA:
                self.state = 159
                self.match(AggregationParser.COMMA)
                self.state = 160
                self.literal()
                self.state = 165
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 166
            self.match(AggregationParser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AggregationParser.RULE_literal

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class StringLiteralContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AggregationParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STR_LITERAL(self):
            return self.getToken(AggregationParser.STR_LITERAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringLiteral" ):
                listener.enterStringLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringLiteral" ):
                listener.exitStringLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringLiteral" ):
                return visitor.visitStringLiteral(self)
            else:
                return visitor.visitChildren(self)


    class FloatLiteralContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AggregationParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(AggregationParser.FLOAT, 0)
        def NUMBER(self):
            return self.getToken(AggregationParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloatLiteral" ):
                listener.enterFloatLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloatLiteral" ):
                listener.exitFloatLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloatLiteral" ):
                return visitor.visitFloatLiteral(self)
            else:
                return visitor.visitChildren(self)



    def literal(self):

        localctx = AggregationParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.state = 170
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [AggregationParser.NUMBER, AggregationParser.FLOAT]:
                localctx = AggregationParser.FloatLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 168
                _la = self._input.LA(1)
                if not(_la==AggregationParser.NUMBER or _la==AggregationParser.FLOAT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [AggregationParser.STR_LITERAL]:
                localctx = AggregationParser.StringLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 169
                self.match(AggregationParser.STR_LITERAL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.aggregation_sempred
        self._predicates[2] = self.expression_sempred
        self._predicates[4] = self.condition_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def aggregation_sempred(self, localctx:AggregationContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

    def condition_sempred(self, localctx:ConditionContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         




