grammar cpp_tiny;

prog : (preProc | globalStatement | classStatement)*;

preProc : '#include' '<' NAME ('.' NAME)? '>';

globalStatement : declaration | definition;

declaration : declarationConstant | declarationVariable | declarationFunction;

declarationConstant : 'const' declarationVariable;

declarationVariable : variable ';';

declarationFunction : type functionName '(' ('const'? '&'? variable (',' 'const'? '&'? variable)*)? ')' ';';

definition : definitionConstant | definitionVariable | definitionFunction;

definitionConstant : 'const' definitionVariable;

definitionVariable : variable '=' (expression | arrayValue | new) ';';

definitionFunction : type functionName '(' ('const'? variable (',' 'const'? variable)*)? ')' block;

classStatement : 'class' NAME '{' (declaration | definition | classPermission)* '}';

classPermission : ('public'  | 'protected' | 'private') ':';

variable : type variableName;

expression : expression ('+' | '-') expression
          | expression ('*' | '/') expression
          | expression ('<' | '>' | '<=' | '>=' | '==' | '!=') expression
          | expression ('&&' | '||') expression
          | expression ('&' | '|') expression
          | expression ('<<' | '>>') expression
          | expression ('^' | '%') expression
          | expression '?' expression ':' expression
          | expression '++' | '--'
          | ('++' | '--') expression
          | '(' expression ')'
          | variableName
          | call
          | typevalue;

block : '{' statement* '}';

statement : declaration
         | definition
         | assignment ';'
         | expression ';'
         | call ';'
         | 'if' '(' condition ')' (statement | block) ('else' (statement | block))?
         | 'while' '(' condition ')' (statement | block)
         | 'for' '(' forInit condition? ';' forIter? ')' (statement | block)
         | 'return' expression ';';

condition : expression;

forInit : (declarationVariable | definitionVariable | statement | ';');

forIter : expression | assignment;

assignment : variableName '=' (expression | arrayValue | new);

call : (variableName | NAME) '(' (expression (',' expression)*)? ')';

type : simpleType | arrayType;

simpleType : 'int' | 'float' | 'char' | 'void' | 'bool' | NAME;

arrayType : simpleType '[' expression? ']';

typevalue : INT | FLOAT | CHAR | STR | BOOL;

variableName : (nameSpace '::')? (parentName '.')* ('*' | '&')?(simpleVariable | arrayVariable);

simpleVariable : NAME;

arrayVariable : NAME ('[' expression? ']')+;

arrayValue : '{' (arrayValue (',' arrayValue)*)? '}' | expression;

new : 'new' type ('[' expression ']')?;

functionName : (nameSpace '::')? (parentName '.')* NAME;

parentName: simpleVariable | arrayVariable | NAME ('('(expression (',' expression)*)?')')?;

nameSpace : NAME;

NAME : [a-zA-Z_][a-zA-Z_0-9]*;

INT : [0-9]+;

FLOAT : [0-9]* '.' [0-9]+;

CHAR : '\'' (. | '\\' .+?) '\'';

STR : '"' .+? '"';

BOOL : 'true' | 'false';

Skip : [ \t\r\n]+ -> skip;

CommentLine : '//' ~[\r\n]* -> skip;

CommentBlock : '/*' .*? '*/' -> skip;