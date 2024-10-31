# Generated from ./parser/cpp_tiny.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .cpp_tinyParser import cpp_tinyParser
else:
    from cpp_tinyParser import cpp_tinyParser

# This class defines a complete generic visitor for a parse tree produced by cpp_tinyParser.

class cpp_tinyVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by cpp_tinyParser#prog.
    def visitProg(self, ctx:cpp_tinyParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp_tinyParser#preProc.
    def visitPreProc(self, ctx:cpp_tinyParser.PreProcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp_tinyParser#globalStatement.
    def visitGlobalStatement(self, ctx:cpp_tinyParser.GlobalStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp_tinyParser#declaration.
    def visitDeclaration(self, ctx:cpp_tinyParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp_tinyParser#declarationConstant.
    def visitDeclarationConstant(self, ctx:cpp_tinyParser.DeclarationConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp_tinyParser#declarationVariable.
    def visitDeclarationVariable(self, ctx:cpp_tinyParser.DeclarationVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp_tinyParser#declarationFunction.
    def visitDeclarationFunction(self, ctx:cpp_tinyParser.DeclarationFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp_tinyParser#definition.
    def visitDefinition(self, ctx:cpp_tinyParser.DefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp_tinyParser#definitionConstant.
    def visitDefinitionConstant(self, ctx:cpp_tinyParser.DefinitionConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp_tinyParser#definitionVariable.
    def visitDefinitionVariable(self, ctx:cpp_tinyParser.DefinitionVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp_tinyParser#definitionFunction.
    def visitDefinitionFunction(self, ctx:cpp_tinyParser.DefinitionFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp_tinyParser#classStatement.
    def visitClassStatement(self, ctx:cpp_tinyParser.ClassStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp_tinyParser#classPermission.
    def visitClassPermission(self, ctx:cpp_tinyParser.ClassPermissionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp_tinyParser#variable.
    def visitVariable(self, ctx:cpp_tinyParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp_tinyParser#expression.
    def visitExpression(self, ctx:cpp_tinyParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp_tinyParser#block.
    def visitBlock(self, ctx:cpp_tinyParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp_tinyParser#statement.
    def visitStatement(self, ctx:cpp_tinyParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp_tinyParser#condition.
    def visitCondition(self, ctx:cpp_tinyParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp_tinyParser#forInit.
    def visitForInit(self, ctx:cpp_tinyParser.ForInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp_tinyParser#forIter.
    def visitForIter(self, ctx:cpp_tinyParser.ForIterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp_tinyParser#assignment.
    def visitAssignment(self, ctx:cpp_tinyParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp_tinyParser#call.
    def visitCall(self, ctx:cpp_tinyParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp_tinyParser#type.
    def visitType(self, ctx:cpp_tinyParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp_tinyParser#simpleType.
    def visitSimpleType(self, ctx:cpp_tinyParser.SimpleTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp_tinyParser#arrayType.
    def visitArrayType(self, ctx:cpp_tinyParser.ArrayTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp_tinyParser#typevalue.
    def visitTypevalue(self, ctx:cpp_tinyParser.TypevalueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp_tinyParser#variableName.
    def visitVariableName(self, ctx:cpp_tinyParser.VariableNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp_tinyParser#simpleVariable.
    def visitSimpleVariable(self, ctx:cpp_tinyParser.SimpleVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp_tinyParser#arrayVariable.
    def visitArrayVariable(self, ctx:cpp_tinyParser.ArrayVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp_tinyParser#arrayValue.
    def visitArrayValue(self, ctx:cpp_tinyParser.ArrayValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp_tinyParser#new.
    def visitNew(self, ctx:cpp_tinyParser.NewContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp_tinyParser#functionName.
    def visitFunctionName(self, ctx:cpp_tinyParser.FunctionNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp_tinyParser#parentName.
    def visitParentName(self, ctx:cpp_tinyParser.ParentNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp_tinyParser#nameSpace.
    def visitNameSpace(self, ctx:cpp_tinyParser.NameSpaceContext):
        return self.visitChildren(ctx)



del cpp_tinyParser