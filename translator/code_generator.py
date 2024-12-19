# generate python code from the AST

class CodeGenerator:

    def add_tab(self, code, num_tabs=1):
        return ["\t" * num_tabs + line for line in code]
    
    def generate_function_call(self, statement):
        code = []
        if statement["name"] == "printf":
            arg = statement['arguments'][0]['value']
            if len(statement['arguments']) > 1:
                arg = arg + " % ("
                for i in range(1, len(statement['arguments'])):
                    arg = arg + statement['arguments'][i]['value']
                    if i < len(statement['arguments']) - 1:
                        arg = arg + ", "
                arg = arg + ")"
            code.append(f"print({arg}, end='')")
        elif statement["name"] == "scanf":
            for i in range(1, len(statement['arguments'])):
                code.append(f"{statement['arguments'][i]['value']} = input()")
        elif statement["name"] == "strlen":
            code.append(f"len({statement['arguments'][0]['value']})")
        return code

    def generate_expression(self, expression):
        if expression["value"] == "true":
            return "True"
        elif expression["value"] == "false":
            return "False"
        elif not isinstance(expression["value"], str):
            node = expression["value"]
            if node['node'] == 'FunctionCall':
                code = self.generate_function_call(node)
                return code[0]
            else:
                return node['value']
        else:
            return expression["value"]

    def generate_statement(self, statement):
        code = []
        if statement["node"] == "FunctionCall":
            code += self.generate_function_call(statement)
        elif statement["node"] == "IfStatement":
            code.append(f"if {statement['condition']}:")
            code += self.add_tab(self.generate_function_block(statement['block']), 1)
            if statement['elseblock']:
                code.append("else:")
                code += self.add_tab(self.generate_function_block(statement['elseblock']), 1)
        elif statement["node"] == "ForLoop":
            code += self.generate_statement(statement["init"])
            code.append(f"while {statement['condition']['value']}:")
            code += self.add_tab(self.generate_function_block(statement["block"]), 1)
            code += self.add_tab(self.generate_statement(statement["update"]), 1)
        elif statement["node"] == "ReturnStatement":
            code.append(f"return {self.generate_expression(statement['value'])}")
        elif statement["node"] == "VariableDefinition":
            if statement["value"]:
                code.append(f"{statement['name']} = {self.generate_expression(statement['value'])}")
        elif statement["node"] == "Expression":
            code.append(self.generate_expression(statement))

        return code

    def generate_function_block(self, block):
        code = []
        for statement in block:
            code += self.generate_statement(statement)
        return code

    def generate(self, ast):
        code = []
        for node in ast:
            if node["node"] == "FunctionDefinition":
                args = node['arguments']
                code.append(f"def {node['name']}({', '.join(args)}):")
                code += self.add_tab(self.generate_function_block(node["block"]), 1)
                code += [""]
        code += ["if __name__ == '__main__':"]
        code += self.add_tab(["main()"])
        return "\n".join(code)

