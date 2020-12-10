grammar Aggregation;

/*
 * Parser
 */
aggregationStatement: aggregation EOF;
aggregation
 : aggregation ARITHMOPERATOR aggregation #AggregationBinOp
 | LPAREN aggregation RPAREN #AggregationGroup
 | AGGR LPAREN expression (COMMA condition)* RPAREN #Reduction
 | COUNT LPAREN category (COMMA condition)* RPAREN #Count
 | CUMAGGR LPAREN SORT ID_LITERAL COMMA expression (COMMA condition)* RPAREN #CumReduction
 | ROLAGGR LPAREN NUMBER COMMA SORT ID_LITERAL COMMA expression (COMMA condition)* RPAREN #RolReduction
 | expression #IdentityAggregation
 ;
expression
 : expression ARITHMOPERATOR expression #ExpressionBinOp
 | LPAREN expression RPAREN #ExpressionGroup
 | measure #IdentityExpression
 ;
conditionStatement: condition EOF;
condition
 : condition SETOPERATOR condition #ConditionBinOp
 | LPAREN condition RPAREN #ConditionGroup
 | NOT LPAREN condition RPAREN #ConditionNegate
 | selector #IdentityCondition
 ;
selector
 :ORDEROPERATOR LPAREN category COMMA literal RPAREN #SelectorOrder
 |IN LPAREN category COMMA literals RPAREN #SelectorIn
 ;
measure
 : (FLOAT|NUMBER) #ConstantMeasure
 | ID_LITERAL #ReferenceMeasure
 ;
category
 : ID_LITERAL #ReferenceCategory
 ;
literals
 :LBRACK  literal ( COMMA literal )* RBRACK
 ;
literal
 : (FLOAT|NUMBER) #FloatLiteral
 | STR_LITERAL #StringLiteral
 ;


/*
 *Lexer
 */
fragment DIGIT       : [0-9] ;
NUMBER               : DIGIT+;
FLOAT                : DIGIT+ ([.] DIGIT+)? ;
fragment LETTER      : [A-Za-z];
SORT                 : ('ASC'|'DESC');
AGGR                 : ('SUM' | 'PROD' | 'MAX' | 'MIN' | 'AVG' | 'VAR' | 'STD');
CUMAGGR              : ('CUMSUM' | 'CUMPROD' | 'CUMMAX' | 'CUMMIN');
ROLAGGR              : ('ROLSUM' | 'ROLPROD' | 'ROLMAX' | 'ROLMIN');
COUNT                : ('COUNT' | 'UCOUNT');
ORDEROPERATOR        : ('EQ' | 'GTE' | 'GT' | 'LT' | 'LTE');
IN                   : 'IN';
NOT                  : 'NOT';
SETOPERATOR          : ('AND'|'OR');
ARITHMOPERATOR       : ('+' | '-' | '*' | '/');
LPAREN               : '(';
RPAREN               : ')';
LBRACK               : '[';
RBRACK               : ']';
COMMA                : ',';
ID_LITERAL           : '\'' [a-zA-Z0-9_\-.] ([a-zA-Z0-9_\-.]| ' ')* '\'';
STR_LITERAL          : '"' (~('"' | '\\' | '\r' | '\n') | '\\' ('"' | '\\'))* '"';
WS                   : (' ' | '\t' | '\r'| '\n') -> skip;