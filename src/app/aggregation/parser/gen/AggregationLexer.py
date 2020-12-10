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
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\26")
        buf.write("\u00ea\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\3\2\3\2")
        buf.write("\3\3\6\3\63\n\3\r\3\16\3\64\3\4\6\48\n\4\r\4\16\49\3\4")
        buf.write("\3\4\6\4>\n\4\r\4\16\4?\5\4B\n\4\3\5\3\5\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\5\6M\n\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\5\7e\n\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\5\b\u0080\n\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\5\t\u009b\n\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\5\n\u00a8\n\n\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u00b6\n\13\3")
        buf.write("\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\5")
        buf.write("\16\u00c4\n\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22")
        buf.write("\3\23\3\23\3\24\3\24\3\25\3\25\3\25\7\25\u00d5\n\25\f")
        buf.write("\25\16\25\u00d8\13\25\3\25\3\25\3\26\3\26\3\26\3\26\7")
        buf.write("\26\u00e0\n\26\f\26\16\26\u00e3\13\26\3\26\3\26\3\27\3")
        buf.write("\27\3\27\3\27\2\2\30\3\2\5\3\7\4\t\2\13\5\r\6\17\7\21")
        buf.write("\b\23\t\25\n\27\13\31\f\33\r\35\16\37\17!\20#\21%\22\'")
        buf.write("\23)\24+\25-\26\3\2\13\3\2\62;\3\2\60\60\4\2C\\c|\5\2")
        buf.write(",-//\61\61\7\2/\60\62;C\\aac|\b\2\"\"/\60\62;C\\aac|\6")
        buf.write("\2\f\f\17\17$$^^\4\2$$^^\5\2\13\f\17\17\"\"\2\u0101\2")
        buf.write("\5\3\2\2\2\2\7\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3")
        buf.write("\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2")
        buf.write("\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2")
        buf.write("\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2")
        buf.write("\2\2\2+\3\2\2\2\2-\3\2\2\2\3/\3\2\2\2\5\62\3\2\2\2\7\67")
        buf.write("\3\2\2\2\tC\3\2\2\2\13L\3\2\2\2\rd\3\2\2\2\17\177\3\2")
        buf.write("\2\2\21\u009a\3\2\2\2\23\u00a7\3\2\2\2\25\u00b5\3\2\2")
        buf.write("\2\27\u00b7\3\2\2\2\31\u00ba\3\2\2\2\33\u00c3\3\2\2\2")
        buf.write("\35\u00c5\3\2\2\2\37\u00c7\3\2\2\2!\u00c9\3\2\2\2#\u00cb")
        buf.write("\3\2\2\2%\u00cd\3\2\2\2\'\u00cf\3\2\2\2)\u00d1\3\2\2\2")
        buf.write("+\u00db\3\2\2\2-\u00e6\3\2\2\2/\60\t\2\2\2\60\4\3\2\2")
        buf.write("\2\61\63\5\3\2\2\62\61\3\2\2\2\63\64\3\2\2\2\64\62\3\2")
        buf.write("\2\2\64\65\3\2\2\2\65\6\3\2\2\2\668\5\3\2\2\67\66\3\2")
        buf.write("\2\289\3\2\2\29\67\3\2\2\29:\3\2\2\2:A\3\2\2\2;=\t\3\2")
        buf.write("\2<>\5\3\2\2=<\3\2\2\2>?\3\2\2\2?=\3\2\2\2?@\3\2\2\2@")
        buf.write("B\3\2\2\2A;\3\2\2\2AB\3\2\2\2B\b\3\2\2\2CD\t\4\2\2D\n")
        buf.write("\3\2\2\2EF\7C\2\2FG\7U\2\2GM\7E\2\2HI\7F\2\2IJ\7G\2\2")
        buf.write("JK\7U\2\2KM\7E\2\2LE\3\2\2\2LH\3\2\2\2M\f\3\2\2\2NO\7")
        buf.write("U\2\2OP\7W\2\2Pe\7O\2\2QR\7R\2\2RS\7T\2\2ST\7Q\2\2Te\7")
        buf.write("F\2\2UV\7O\2\2VW\7C\2\2We\7Z\2\2XY\7O\2\2YZ\7K\2\2Ze\7")
        buf.write("P\2\2[\\\7C\2\2\\]\7X\2\2]e\7I\2\2^_\7X\2\2_`\7C\2\2`")
        buf.write("e\7T\2\2ab\7U\2\2bc\7V\2\2ce\7F\2\2dN\3\2\2\2dQ\3\2\2")
        buf.write("\2dU\3\2\2\2dX\3\2\2\2d[\3\2\2\2d^\3\2\2\2da\3\2\2\2e")
        buf.write("\16\3\2\2\2fg\7E\2\2gh\7W\2\2hi\7O\2\2ij\7U\2\2jk\7W\2")
        buf.write("\2k\u0080\7O\2\2lm\7E\2\2mn\7W\2\2no\7O\2\2op\7R\2\2p")
        buf.write("q\7T\2\2qr\7Q\2\2r\u0080\7F\2\2st\7E\2\2tu\7W\2\2uv\7")
        buf.write("O\2\2vw\7O\2\2wx\7C\2\2x\u0080\7Z\2\2yz\7E\2\2z{\7W\2")
        buf.write("\2{|\7O\2\2|}\7O\2\2}~\7K\2\2~\u0080\7P\2\2\177f\3\2\2")
        buf.write("\2\177l\3\2\2\2\177s\3\2\2\2\177y\3\2\2\2\u0080\20\3\2")
        buf.write("\2\2\u0081\u0082\7T\2\2\u0082\u0083\7Q\2\2\u0083\u0084")
        buf.write("\7N\2\2\u0084\u0085\7U\2\2\u0085\u0086\7W\2\2\u0086\u009b")
        buf.write("\7O\2\2\u0087\u0088\7T\2\2\u0088\u0089\7Q\2\2\u0089\u008a")
        buf.write("\7N\2\2\u008a\u008b\7R\2\2\u008b\u008c\7T\2\2\u008c\u008d")
        buf.write("\7Q\2\2\u008d\u009b\7F\2\2\u008e\u008f\7T\2\2\u008f\u0090")
        buf.write("\7Q\2\2\u0090\u0091\7N\2\2\u0091\u0092\7O\2\2\u0092\u0093")
        buf.write("\7C\2\2\u0093\u009b\7Z\2\2\u0094\u0095\7T\2\2\u0095\u0096")
        buf.write("\7Q\2\2\u0096\u0097\7N\2\2\u0097\u0098\7O\2\2\u0098\u0099")
        buf.write("\7K\2\2\u0099\u009b\7P\2\2\u009a\u0081\3\2\2\2\u009a\u0087")
        buf.write("\3\2\2\2\u009a\u008e\3\2\2\2\u009a\u0094\3\2\2\2\u009b")
        buf.write("\22\3\2\2\2\u009c\u009d\7E\2\2\u009d\u009e\7Q\2\2\u009e")
        buf.write("\u009f\7W\2\2\u009f\u00a0\7P\2\2\u00a0\u00a8\7V\2\2\u00a1")
        buf.write("\u00a2\7W\2\2\u00a2\u00a3\7E\2\2\u00a3\u00a4\7Q\2\2\u00a4")
        buf.write("\u00a5\7W\2\2\u00a5\u00a6\7P\2\2\u00a6\u00a8\7V\2\2\u00a7")
        buf.write("\u009c\3\2\2\2\u00a7\u00a1\3\2\2\2\u00a8\24\3\2\2\2\u00a9")
        buf.write("\u00aa\7G\2\2\u00aa\u00b6\7S\2\2\u00ab\u00ac\7I\2\2\u00ac")
        buf.write("\u00ad\7V\2\2\u00ad\u00b6\7G\2\2\u00ae\u00af\7I\2\2\u00af")
        buf.write("\u00b6\7V\2\2\u00b0\u00b1\7N\2\2\u00b1\u00b6\7V\2\2\u00b2")
        buf.write("\u00b3\7N\2\2\u00b3\u00b4\7V\2\2\u00b4\u00b6\7G\2\2\u00b5")
        buf.write("\u00a9\3\2\2\2\u00b5\u00ab\3\2\2\2\u00b5\u00ae\3\2\2\2")
        buf.write("\u00b5\u00b0\3\2\2\2\u00b5\u00b2\3\2\2\2\u00b6\26\3\2")
        buf.write("\2\2\u00b7\u00b8\7K\2\2\u00b8\u00b9\7P\2\2\u00b9\30\3")
        buf.write("\2\2\2\u00ba\u00bb\7P\2\2\u00bb\u00bc\7Q\2\2\u00bc\u00bd")
        buf.write("\7V\2\2\u00bd\32\3\2\2\2\u00be\u00bf\7C\2\2\u00bf\u00c0")
        buf.write("\7P\2\2\u00c0\u00c4\7F\2\2\u00c1\u00c2\7Q\2\2\u00c2\u00c4")
        buf.write("\7T\2\2\u00c3\u00be\3\2\2\2\u00c3\u00c1\3\2\2\2\u00c4")
        buf.write("\34\3\2\2\2\u00c5\u00c6\t\5\2\2\u00c6\36\3\2\2\2\u00c7")
        buf.write("\u00c8\7*\2\2\u00c8 \3\2\2\2\u00c9\u00ca\7+\2\2\u00ca")
        buf.write("\"\3\2\2\2\u00cb\u00cc\7]\2\2\u00cc$\3\2\2\2\u00cd\u00ce")
        buf.write("\7_\2\2\u00ce&\3\2\2\2\u00cf\u00d0\7.\2\2\u00d0(\3\2\2")
        buf.write("\2\u00d1\u00d2\7)\2\2\u00d2\u00d6\t\6\2\2\u00d3\u00d5")
        buf.write("\t\7\2\2\u00d4\u00d3\3\2\2\2\u00d5\u00d8\3\2\2\2\u00d6")
        buf.write("\u00d4\3\2\2\2\u00d6\u00d7\3\2\2\2\u00d7\u00d9\3\2\2\2")
        buf.write("\u00d8\u00d6\3\2\2\2\u00d9\u00da\7)\2\2\u00da*\3\2\2\2")
        buf.write("\u00db\u00e1\7$\2\2\u00dc\u00e0\n\b\2\2\u00dd\u00de\7")
        buf.write("^\2\2\u00de\u00e0\t\t\2\2\u00df\u00dc\3\2\2\2\u00df\u00dd")
        buf.write("\3\2\2\2\u00e0\u00e3\3\2\2\2\u00e1\u00df\3\2\2\2\u00e1")
        buf.write("\u00e2\3\2\2\2\u00e2\u00e4\3\2\2\2\u00e3\u00e1\3\2\2\2")
        buf.write("\u00e4\u00e5\7$\2\2\u00e5,\3\2\2\2\u00e6\u00e7\t\n\2\2")
        buf.write("\u00e7\u00e8\3\2\2\2\u00e8\u00e9\b\27\2\2\u00e9.\3\2\2")
        buf.write("\2\22\2\649?ALd\177\u009a\u00a7\u00b5\u00c3\u00d4\u00d6")
        buf.write("\u00df\u00e1\3\b\2\2")
        return buf.getvalue()


class AggregationLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    NUMBER = 1
    FLOAT = 2
    SORT = 3
    AGGR = 4
    CUMAGGR = 5
    ROLAGGR = 6
    COUNT = 7
    ORDEROPERATOR = 8
    IN = 9
    NOT = 10
    SETOPERATOR = 11
    ARITHMOPERATOR = 12
    LPAREN = 13
    RPAREN = 14
    LBRACK = 15
    RBRACK = 16
    COMMA = 17
    ID_LITERAL = 18
    STR_LITERAL = 19
    WS = 20

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'IN'", "'NOT'", "'('", "')'", "'['", "']'", "','" ]

    symbolicNames = [ "<INVALID>",
            "NUMBER", "FLOAT", "SORT", "AGGR", "CUMAGGR", "ROLAGGR", "COUNT", 
            "ORDEROPERATOR", "IN", "NOT", "SETOPERATOR", "ARITHMOPERATOR", 
            "LPAREN", "RPAREN", "LBRACK", "RBRACK", "COMMA", "ID_LITERAL", 
            "STR_LITERAL", "WS" ]

    ruleNames = [ "DIGIT", "NUMBER", "FLOAT", "LETTER", "SORT", "AGGR", 
                  "CUMAGGR", "ROLAGGR", "COUNT", "ORDEROPERATOR", "IN", 
                  "NOT", "SETOPERATOR", "ARITHMOPERATOR", "LPAREN", "RPAREN", 
                  "LBRACK", "RBRACK", "COMMA", "ID_LITERAL", "STR_LITERAL", 
                  "WS" ]

    grammarFileName = "Aggregation.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


