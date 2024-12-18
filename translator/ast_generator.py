# generates AST by visiting ANTLR parse tree

from parser.cpp_tinyVisitor import cpp_tinyVisitor

class ASTGenerator(cpp_tinyVisitor):
    def visitProg(self, ctx):
        print(f"\nDebug: Visiting prog node")
        if ctx is None or not ctx.children:
            print("Debug: No children in prog node")
            return []
        nodes = []
        for i, child in enumerate(ctx.children):
            print(f"\nDebug: Visiting child {i} of type {type(child)}")
            print(f"Debug: Child text: {child.getText()}")
            result = self.visit(child)
            print(f"Debug: Result: {result}")
            if result is not None:
                nodes.append(result)
        print(f"\nDebug: Prog node generated {len(nodes)} nodes: {nodes}")
        return nodes if nodes else None

    def visitGlobalStatement(self, ctx):
        print("\nDebug: Visiting global statement")
        if ctx is None:
            return None
        # A global statement can contain a declaration or definition
        if ctx.declaration():
            print("Debug: Found declaration")
            return self.visit(ctx.declaration())
        elif ctx.definition():
            print("Debug: Found definition")
            return self.visit(ctx.definition())
        print("Debug: No declaration or definition found")
        return None

    def visitDefinition(self, ctx):
        print(f"\nDebug: Visiting definition")
        if ctx is None:
            return None
        if ctx.definitionVariable():
            print("Debug: Found variable definition")
            return self.visit(ctx.definitionVariable())
        return None

    def visitDefinitionVariable(self, ctx):
        print(f"\nDebug: Visiting definition variable")
        if ctx is None:
            return None
        
        # Get variable type and name
        var = self.visit(ctx.variable())
        if var is None:
            return None
        
        # Get the expression/value
        value = None
        if ctx.expression():
            value = self.visit(ctx.expression())
        elif ctx.arrayValue():
            value = self.visit(ctx.arrayValue())
        elif ctx.new():
            value = self.visit(ctx.new())

        return {
            "node": "VariableDefinition",
            "type": var["type"],
            "name": var["name"],
            "value": value
        }

    def visitVariable(self, ctx):
        if ctx is None:
            return None
        var_type = ctx.type().getText() if ctx.type() else ""
        var_name = ctx.variableName().getText() if ctx.variableName() else ""
        return {"type": var_type, "name": var_name}

    def visitExpression(self, ctx):
        print(f"\nDebug: Visiting expression: {ctx.getText()}")
        if ctx is None:
            return None
        
        # Binary operations
        if ctx.PLUS():
            return {
                "node": "BinaryOperation",
                "operator": "+",
                "left": self.visit(ctx.expression(0)),
                "right": self.visit(ctx.expression(1))
            }
        
        # Variable reference
        if ctx.variableName():
            return {"node": "Variable", "name": ctx.variableName().getText()}
        
        # Literal values
        if ctx.INT():
            return {"node": "Literal", "type": "int", "value": ctx.INT().getText()}
        elif ctx.FLOAT():
            return {"node": "Literal", "type": "float", "value": ctx.FLOAT().getText()}
        
        return self.visitChildren(ctx)
