# generates AST by visiting ANTLR parse tree

from parser.cpp_tinyVisitor import cpp_tinyVisitor
from parser.cpp_tinyParser import cpp_tinyParser

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
        elif ctx.definitionFunction():
            print("Debug: Found function definition")
            return self.visit(ctx.definitionFunction())
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


    def visitDefinitionFunction(self, ctx):
        print(f"\nDebug: Visiting definition function")
        if ctx is None:
            return None
        returntype = ctx.type_().getText() if ctx.type_() else ""
        functionname = ctx.functionName().getText() if ctx.functionName() else ""
        # TODO: arguments
        variables = []
        i = 0
        var = ctx.variable(i)
        while var:
            variables.append(var.variableName().getText())
            i += 1
            var = ctx.variable(i)
        block = self.visit(ctx.block())
        return {
            "node": "FunctionDefinition",
            "type": returntype,
            "name": functionname,
            "arguments": variables,
            "block": block
        }
    
    def visitBlock(self, ctx):
        print(f"\nDebug: Visiting block")
        if ctx is None:
            return None
        nodes = []
        for i, child in enumerate(ctx.children):
            print(f"\nDebug: Visiting child {i} of type {type(child)}")
            print(f"Debug: Child text: {child.getText()}")
            result = self.visit(child)
            print(f"Debug: Result: {result}")
            if result is not None:
                nodes.append(result)
        print(f"\nDebug: Block node generated {len(nodes)} nodes: {nodes}")
        return nodes if nodes else None
    
    def visitStatement(self, ctx):
        print(f"\nDebug: Visiting statement")
        if ctx is None:
            return None
        if ctx.call():
            print("Debug: call")
            return self.visit(ctx.call())
        elif ctx.IF():
            # TODO: if 和 for 暂时不支持单句
            print("Debug: if")
            block = self.visit(ctx.block(0))
            elseblock = self.visit(ctx.block(1)) if ctx.ELSE() else None
            return {
                "node": "IfStatement",
                "condition": ctx.condition().getText(), # TODO: parse condition
                "block": block,
                "elseblock": elseblock
            }
        elif ctx.FOR():
            print("Debug: for")
            return {
                "node": "ForLoop",
                "init": self.visit(ctx.forInit()),
                "condition": self.visit(ctx.condition()),
                "update": self.visit(ctx.forIter()),
                "block": self.visit(ctx.block(0))
            }
        elif ctx.retstat():
            print("Debug: retstat")
            return self.visit(ctx.retstat())
        elif ctx.expression():
            print("Debug: expression")
            return self.visit(ctx.expression())
        elif ctx.definition():
            print("Debug: definition")
            return self.visit(ctx.definition())
        else:
            print("Debug: unknown")
            print(type(ctx.getChild(0)))

    def visitRetstat(self, ctx):
        return {
            "node": "ReturnStatement",
            "value": self.visit(ctx.expression())
        }

    def visitCondition(self, ctx):
        return self.visit(ctx.expression())
    
    def visitCall(self, ctx):
        print(f"\nDebug: Visiting call")
        if ctx is None:
            return None
        functionname = ctx.variableName().getText() if ctx.variableName() else ctx.NAME().getText()
        arguments = []
        for i in range(1, ctx.getChildCount() - 1):
            arg = self.visit(ctx.getChild(i))
            if arg is not None:
                arguments.append(arg)
        return {
            "node": "FunctionCall",
            "name": functionname,
            "arguments": arguments
        }

    def visitVariable(self, ctx):
        if ctx is None:
            return None
        var_type = ctx.type_().getText() if ctx.type_() else ""
        var_name = ctx.variableName().getText() if ctx.variableName() else ""
        return {"type": var_type, "name": var_name}

    def visitExpression(self, ctx):
        print(f"\nDebug: Visiting expression: {ctx.getText()}")
        if ctx is None:
            return None
        
        if ctx.call():
            return {
                "node": "Expression",
                "value": self.visit(ctx.call())
            }
        
        return {
            "node": "Expression",
            "value": ctx.getText()
        }

        # TODO: better parse
        # # Binary operations
        # if ctx.PLUS():
        #     return {
        #         "node": "BinaryOperation",
        #         "operator": "+",
        #         "left": self.visit(ctx.expression(0)),
        #         "right": self.visit(ctx.expression(1))
        #     }
        
        # # Variable reference
        # if ctx.variableName():
        #     return {"node": "Variable", "name": ctx.variableName().getText()}
        
        # # Literal values
        # if ctx.typevalue():
        #     return self.visit(ctx.typevalue())
        
        # return self.visitChildren(ctx)

    def visitTypevalue(self, ctx):
        if ctx is None:
            return None
        if ctx.INT():
            return {"node": "Literal", "type": "int", "value": int(ctx.INT().getText())}
        if ctx.FLOAT():
            return {"node": "Literal", "type": "float", "value": float(ctx.FLOAT().getText())}
        if ctx.STR():
            return {"node": "Literal", "type": "string", "value": ctx.STR().getText()}
        return None
