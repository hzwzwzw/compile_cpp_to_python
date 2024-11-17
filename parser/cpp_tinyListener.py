# Generated from ./cpp_tiny.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .cpp_tinyParser import cpp_tinyParser
else:
    from cpp_tinyParser import cpp_tinyParser

# This class defines a complete listener for a parse tree produced by cpp_tinyParser.
class cpp_tinyListener(ParseTreeListener):

    # Enter a parse tree produced by cpp_tinyParser#prog.
    def enterProg(self, ctx:cpp_tinyParser.ProgContext):
        pass

    # Exit a parse tree produced by cpp_tinyParser#prog.
    def exitProg(self, ctx:cpp_tinyParser.ProgContext):
        pass


    # Enter a parse tree produced by cpp_tinyParser#preProc.
    def enterPreProc(self, ctx:cpp_tinyParser.PreProcContext):
        pass

    # Exit a parse tree produced by cpp_tinyParser#preProc.
    def exitPreProc(self, ctx:cpp_tinyParser.PreProcContext):
        pass


    # Enter a parse tree produced by cpp_tinyParser#globalStatement.
    def enterGlobalStatement(self, ctx:cpp_tinyParser.GlobalStatementContext):
        pass

    # Exit a parse tree produced by cpp_tinyParser#globalStatement.
    def exitGlobalStatement(self, ctx:cpp_tinyParser.GlobalStatementContext):
        pass


    # Enter a parse tree produced by cpp_tinyParser#declaration.
    def enterDeclaration(self, ctx:cpp_tinyParser.DeclarationContext):
        pass

    # Exit a parse tree produced by cpp_tinyParser#declaration.
    def exitDeclaration(self, ctx:cpp_tinyParser.DeclarationContext):
        pass


    # Enter a parse tree produced by cpp_tinyParser#declarationConstant.
    def enterDeclarationConstant(self, ctx:cpp_tinyParser.DeclarationConstantContext):
        pass

    # Exit a parse tree produced by cpp_tinyParser#declarationConstant.
    def exitDeclarationConstant(self, ctx:cpp_tinyParser.DeclarationConstantContext):
        pass


    # Enter a parse tree produced by cpp_tinyParser#declarationVariable.
    def enterDeclarationVariable(self, ctx:cpp_tinyParser.DeclarationVariableContext):
        pass

    # Exit a parse tree produced by cpp_tinyParser#declarationVariable.
    def exitDeclarationVariable(self, ctx:cpp_tinyParser.DeclarationVariableContext):
        pass


    # Enter a parse tree produced by cpp_tinyParser#declarationFunction.
    def enterDeclarationFunction(self, ctx:cpp_tinyParser.DeclarationFunctionContext):
        pass

    # Exit a parse tree produced by cpp_tinyParser#declarationFunction.
    def exitDeclarationFunction(self, ctx:cpp_tinyParser.DeclarationFunctionContext):
        pass


    # Enter a parse tree produced by cpp_tinyParser#definition.
    def enterDefinition(self, ctx:cpp_tinyParser.DefinitionContext):
        pass

    # Exit a parse tree produced by cpp_tinyParser#definition.
    def exitDefinition(self, ctx:cpp_tinyParser.DefinitionContext):
        pass


    # Enter a parse tree produced by cpp_tinyParser#definitionConstant.
    def enterDefinitionConstant(self, ctx:cpp_tinyParser.DefinitionConstantContext):
        pass

    # Exit a parse tree produced by cpp_tinyParser#definitionConstant.
    def exitDefinitionConstant(self, ctx:cpp_tinyParser.DefinitionConstantContext):
        pass


    # Enter a parse tree produced by cpp_tinyParser#definitionVariable.
    def enterDefinitionVariable(self, ctx:cpp_tinyParser.DefinitionVariableContext):
        pass

    # Exit a parse tree produced by cpp_tinyParser#definitionVariable.
    def exitDefinitionVariable(self, ctx:cpp_tinyParser.DefinitionVariableContext):
        pass


    # Enter a parse tree produced by cpp_tinyParser#definitionFunction.
    def enterDefinitionFunction(self, ctx:cpp_tinyParser.DefinitionFunctionContext):
        pass

    # Exit a parse tree produced by cpp_tinyParser#definitionFunction.
    def exitDefinitionFunction(self, ctx:cpp_tinyParser.DefinitionFunctionContext):
        pass


    # Enter a parse tree produced by cpp_tinyParser#classStatement.
    def enterClassStatement(self, ctx:cpp_tinyParser.ClassStatementContext):
        pass

    # Exit a parse tree produced by cpp_tinyParser#classStatement.
    def exitClassStatement(self, ctx:cpp_tinyParser.ClassStatementContext):
        pass


    # Enter a parse tree produced by cpp_tinyParser#classPermission.
    def enterClassPermission(self, ctx:cpp_tinyParser.ClassPermissionContext):
        pass

    # Exit a parse tree produced by cpp_tinyParser#classPermission.
    def exitClassPermission(self, ctx:cpp_tinyParser.ClassPermissionContext):
        pass


    # Enter a parse tree produced by cpp_tinyParser#variable.
    def enterVariable(self, ctx:cpp_tinyParser.VariableContext):
        pass

    # Exit a parse tree produced by cpp_tinyParser#variable.
    def exitVariable(self, ctx:cpp_tinyParser.VariableContext):
        pass


    # Enter a parse tree produced by cpp_tinyParser#expression.
    def enterExpression(self, ctx:cpp_tinyParser.ExpressionContext):
        pass

    # Exit a parse tree produced by cpp_tinyParser#expression.
    def exitExpression(self, ctx:cpp_tinyParser.ExpressionContext):
        pass


    # Enter a parse tree produced by cpp_tinyParser#block.
    def enterBlock(self, ctx:cpp_tinyParser.BlockContext):
        pass

    # Exit a parse tree produced by cpp_tinyParser#block.
    def exitBlock(self, ctx:cpp_tinyParser.BlockContext):
        pass


    # Enter a parse tree produced by cpp_tinyParser#statement.
    def enterStatement(self, ctx:cpp_tinyParser.StatementContext):
        pass

    # Exit a parse tree produced by cpp_tinyParser#statement.
    def exitStatement(self, ctx:cpp_tinyParser.StatementContext):
        pass


    # Enter a parse tree produced by cpp_tinyParser#retstat.
    def enterRetstat(self, ctx:cpp_tinyParser.RetstatContext):
        pass

    # Exit a parse tree produced by cpp_tinyParser#retstat.
    def exitRetstat(self, ctx:cpp_tinyParser.RetstatContext):
        pass


    # Enter a parse tree produced by cpp_tinyParser#condition.
    def enterCondition(self, ctx:cpp_tinyParser.ConditionContext):
        pass

    # Exit a parse tree produced by cpp_tinyParser#condition.
    def exitCondition(self, ctx:cpp_tinyParser.ConditionContext):
        pass


    # Enter a parse tree produced by cpp_tinyParser#forInit.
    def enterForInit(self, ctx:cpp_tinyParser.ForInitContext):
        pass

    # Exit a parse tree produced by cpp_tinyParser#forInit.
    def exitForInit(self, ctx:cpp_tinyParser.ForInitContext):
        pass


    # Enter a parse tree produced by cpp_tinyParser#forIter.
    def enterForIter(self, ctx:cpp_tinyParser.ForIterContext):
        pass

    # Exit a parse tree produced by cpp_tinyParser#forIter.
    def exitForIter(self, ctx:cpp_tinyParser.ForIterContext):
        pass


    # Enter a parse tree produced by cpp_tinyParser#assignment.
    def enterAssignment(self, ctx:cpp_tinyParser.AssignmentContext):
        pass

    # Exit a parse tree produced by cpp_tinyParser#assignment.
    def exitAssignment(self, ctx:cpp_tinyParser.AssignmentContext):
        pass


    # Enter a parse tree produced by cpp_tinyParser#call.
    def enterCall(self, ctx:cpp_tinyParser.CallContext):
        pass

    # Exit a parse tree produced by cpp_tinyParser#call.
    def exitCall(self, ctx:cpp_tinyParser.CallContext):
        pass


    # Enter a parse tree produced by cpp_tinyParser#type.
    def enterType(self, ctx:cpp_tinyParser.TypeContext):
        pass

    # Exit a parse tree produced by cpp_tinyParser#type.
    def exitType(self, ctx:cpp_tinyParser.TypeContext):
        pass


    # Enter a parse tree produced by cpp_tinyParser#simpleType.
    def enterSimpleType(self, ctx:cpp_tinyParser.SimpleTypeContext):
        pass

    # Exit a parse tree produced by cpp_tinyParser#simpleType.
    def exitSimpleType(self, ctx:cpp_tinyParser.SimpleTypeContext):
        pass


    # Enter a parse tree produced by cpp_tinyParser#arrayType.
    def enterArrayType(self, ctx:cpp_tinyParser.ArrayTypeContext):
        pass

    # Exit a parse tree produced by cpp_tinyParser#arrayType.
    def exitArrayType(self, ctx:cpp_tinyParser.ArrayTypeContext):
        pass


    # Enter a parse tree produced by cpp_tinyParser#typevalue.
    def enterTypevalue(self, ctx:cpp_tinyParser.TypevalueContext):
        pass

    # Exit a parse tree produced by cpp_tinyParser#typevalue.
    def exitTypevalue(self, ctx:cpp_tinyParser.TypevalueContext):
        pass


    # Enter a parse tree produced by cpp_tinyParser#variableName.
    def enterVariableName(self, ctx:cpp_tinyParser.VariableNameContext):
        pass

    # Exit a parse tree produced by cpp_tinyParser#variableName.
    def exitVariableName(self, ctx:cpp_tinyParser.VariableNameContext):
        pass


    # Enter a parse tree produced by cpp_tinyParser#simpleVariable.
    def enterSimpleVariable(self, ctx:cpp_tinyParser.SimpleVariableContext):
        pass

    # Exit a parse tree produced by cpp_tinyParser#simpleVariable.
    def exitSimpleVariable(self, ctx:cpp_tinyParser.SimpleVariableContext):
        pass


    # Enter a parse tree produced by cpp_tinyParser#arrayVariable.
    def enterArrayVariable(self, ctx:cpp_tinyParser.ArrayVariableContext):
        pass

    # Exit a parse tree produced by cpp_tinyParser#arrayVariable.
    def exitArrayVariable(self, ctx:cpp_tinyParser.ArrayVariableContext):
        pass


    # Enter a parse tree produced by cpp_tinyParser#arrayValue.
    def enterArrayValue(self, ctx:cpp_tinyParser.ArrayValueContext):
        pass

    # Exit a parse tree produced by cpp_tinyParser#arrayValue.
    def exitArrayValue(self, ctx:cpp_tinyParser.ArrayValueContext):
        pass


    # Enter a parse tree produced by cpp_tinyParser#new.
    def enterNew(self, ctx:cpp_tinyParser.NewContext):
        pass

    # Exit a parse tree produced by cpp_tinyParser#new.
    def exitNew(self, ctx:cpp_tinyParser.NewContext):
        pass


    # Enter a parse tree produced by cpp_tinyParser#functionName.
    def enterFunctionName(self, ctx:cpp_tinyParser.FunctionNameContext):
        pass

    # Exit a parse tree produced by cpp_tinyParser#functionName.
    def exitFunctionName(self, ctx:cpp_tinyParser.FunctionNameContext):
        pass


    # Enter a parse tree produced by cpp_tinyParser#parentName.
    def enterParentName(self, ctx:cpp_tinyParser.ParentNameContext):
        pass

    # Exit a parse tree produced by cpp_tinyParser#parentName.
    def exitParentName(self, ctx:cpp_tinyParser.ParentNameContext):
        pass


    # Enter a parse tree produced by cpp_tinyParser#nameSpace.
    def enterNameSpace(self, ctx:cpp_tinyParser.NameSpaceContext):
        pass

    # Exit a parse tree produced by cpp_tinyParser#nameSpace.
    def exitNameSpace(self, ctx:cpp_tinyParser.NameSpaceContext):
        pass



del cpp_tinyParser