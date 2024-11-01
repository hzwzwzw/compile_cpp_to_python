grammar cpp_tiny;

prog : (preProc | globalStatement | classStatement)*;

preProc : INCLUDE LESS NAME (DOT NAME)? GREATER
        | INCLUDE QUOTE NAME (DOT NAME)? QUOTE;


globalStatement : declaration | definition;

declaration : declarationConstant | declarationVariable | declarationFunction;

declarationConstant : CONSTANT declarationVariable;

declarationVariable : variable SEMICOLON;

declarationFunction : type functionName L_BRACKET (CONSTANT? AND? variable (COMMA CONSTANT? AND? variable)*)? R_BRACKET SEMICOLON;

definition : definitionConstant | definitionVariable | definitionFunction;

definitionConstant : CONSTANT definitionVariable;

definitionVariable : variable ASSIGN (expression | arrayValue | new) SEMICOLON;

definitionFunction : type functionName L_BRACKET (CONSTANT? variable (COMMA CONSTANT? variable)*)? R_BRACKET block;

classStatement : CLASS NAME L_BRACE (declaration | definition | classPermission)* R_BRACE;

classPermission : (PERMISSON_PUBLIC | PERMISSON_PROTECTED | PERMISSON_PRIVATE) COLON;

variable : type variableName;

expression : expression (PLUS | MINUS) expression
          | expression (MULTIPLY | DIVIDE) expression
          | expression (LESS | GREATER | LEQ | GEQ | NOT_EQUAL) expression
          | expression (DOUBLE_AND | DOUBLE_OR) expression
          | expression (AND | OR) expression
          | expression (SHIFT_LEFT | SHIFT_RIGHT) expression
          | expression (XOR | MODULO) expression
          | expression QUESTION expression COLON expression
          | NOT expression
          | expression (DOUBLE_PLUS | DOUBLE_MINUS)
          | (DOUBLE_PLUS | DOUBLE_MINUS) expression
          | L_BRACKET expression R_BRACKET
          | variableName
          | call
          | typevalue;

block : L_BRACE statement* R_BRACE;

statement : declaration
         | definition
         | assignment SEMICOLON
         | expression SEMICOLON
         | call SEMICOLON
         | IF L_BRACKET condition R_BRACKET (statement | block) (ELSE (statement | block))?
         | WHILE L_BRACKET condition R_BRACKET (statement | block)
         | FOR L_BRACKET forInit condition? SEMICOLON forIter? R_BRACKET (statement | block)
         | RETURN expression SEMICOLON;

condition : expression;

forInit : (declarationVariable | definitionVariable | statement | SEMICOLON);

forIter : expression | assignment;

assignment : variableName ASSIGN (expression | arrayValue | new);

call : (variableName | NAME) L_BRACKET (expression (COMMA expression)*)? R_BRACKET;

type : simpleType | arrayType;

simpleType : TYPE_INT | TYPE_FLOAT | TYPE_DOUBLE | TYPE_BOOL | TYPE_CHAR | TYPE_VOID | NAME;

arrayType : simpleType L_SQUARE_BRACKET expression? R_SQUARE_BRACKET;

typevalue : INT | FLOAT | CHAR | STR | BOOL;

variableName : (nameSpace DOUBLE_COLON)? (parentName DOT)* (MULTIPLY | AND)?(simpleVariable | arrayVariable);

simpleVariable : NAME;

arrayVariable : NAME (L_SQUARE_BRACKET expression? R_SQUARE_BRACKET)+;

arrayValue : L_BRACE (arrayValue (COMMA arrayValue)*)? R_BRACE | expression;

new : NEW type (L_SQUARE_BRACKET expression R_SQUARE_BRACKET)?;

functionName : (nameSpace DOUBLE_COLON)? (parentName DOT)* NAME;

parentName: simpleVariable | arrayVariable | NAME (L_BRACKET (expression (COMMA expression)*)? R_BRACKET)?;

nameSpace : NAME;

NAME : [a-zA-Z_][a-zA-Z_0-9]*;

INT : [0-9]+;

FLOAT : [0-9]* '.' [0-9]+;

CHAR : '\'' (. | '\\' .+?) '\'';

STR : QUOTE .+? QUOTE;

BOOL : 'true' | 'false';

TYPE_INT : 'int';

TYPE_FLOAT : 'float';

TYPE_DOUBLE : 'double';

TYPE_CHAR : 'char';

TYPE_VOID : 'void';

TYPE_BOOL : 'bool';

IF : 'if';

ELSE : 'else';

FOR : 'for';

WHILE : 'while';

RETURN : 'return';

NEW : 'new';

INCLUDE : '#include';

L_BRACKET : '(';

R_BRACKET : ')';

L_BRACE : '{';

R_BRACE : '}';

L_SQUARE_BRACKET : '[';

R_SQUARE_BRACKET : ']';

QUOTE : '"';

COMMA : ',';

DOT : '.';

CONSTANT : 'const';

CLASS : 'class';

PERMISSON_PUBLIC : 'public';

PERMISSON_PROTECTED : 'protected';

PERMISSON_PRIVATE : 'private';

COLON : ':';

DOUBLE_COLON : '::';

SEMICOLON : ';';

ASSIGN  : '=';

PLUS : '+';

MINUS : '-';

MULTIPLY : '*';

DIVIDE : '/';

DOUBLE_PLUS : '++';

DOUBLE_MINUS : '--';

MODULO : '%';

AND : '&';

OR : '|';

LESS : '<';

GREATER : '>';

LEQ : '<=';

GEQ : '>=';

EQUAL : '==';

NOT_EQUAL : '!=';

DOUBLE_AND : '&&';

DOUBLE_OR : '||';

NOT : '!';

XOR : '^';

QUESTION : '?';

SHIFT_LEFT : '<<';

SHIFT_RIGHT : '>>';

Skip : [ \t\r\n]+ -> skip;

CommentLine : '//' ~[\r\n]* -> skip;

CommentBlock : '/*' .*? '*/' -> skip;