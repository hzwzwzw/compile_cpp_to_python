# generate python code from the AST

class CodeGenerator:

    def add_tab(self, code, num_tabs=1):
        return ["\t" * num_tabs + line for line in code]

    def generate_function_call(self, statement):
        code = []

        # 处理 printf
        if statement["name"] == "printf":
            format_string = statement["arguments"][0]["value"]
            format_string_converted = format_string.replace("%d", "{}").replace("%f", "{}").replace("%s", "{}")
            has_newline = "\\n" in format_string
            format_string_converted = format_string_converted.replace("\\n", "")
            if len(statement["arguments"]) > 1:
                args = ", ".join([arg["value"] for arg in statement["arguments"][1:]])
                placeholder_count = format_string_converted.count("{}")
                if placeholder_count != len(statement["arguments"]) - 1:
                    raise ValueError(f"Mismatch between format specifiers ({placeholder_count}) and arguments ({len(statement['arguments']) - 1}).")
                if has_newline:
                    code.append(f'print({format_string_converted}.format({args}))')
                else:
                    code.append(f'print({format_string_converted}.format({args}), end="")')
            else:
                if "{}" in format_string_converted:
                    raise ValueError("Format string contains placeholders, but no arguments provided.")
                if has_newline:
                    code.append(f'print({format_string_converted})')
                else:
                    code.append(f'print({format_string_converted}, end="")')

        # 处理 scanf
        elif statement["name"] == "scanf":
            for i in range(1, len(statement["arguments"])):
                code.append(f'{statement["arguments"][i]["value"]} = input()')

        # 处理 strlen
        elif statement["name"] == "strlen":
            code.append(f'len({statement["arguments"][0]["value"]})')

        # 默认函数调用处理
        else:
            arguments = ", ".join([arg["value"] for arg in statement["arguments"]])
            code.append(f'{statement["name"]}({arguments})')

        return code

    def generate_expression(self, expression):
        while isinstance(expression.get("value"), dict) and expression["value"].get("node") == "Expression":
            expression = expression["value"]

        # 处理 sizeof 运算符
        if "sizeof" in expression["value"]:
            if "/" in expression["value"]:
                parts = expression["value"].split("/")
                if "sizeof" in parts[0] and "sizeof" in parts[1]:
                    array_name = parts[0].strip().replace("sizeof(", "").replace(")", "")
                    return f"len({array_name})"
            else:
                array_name = expression["value"].replace("sizeof(", "").replace(")", "").strip()
                return f"len({array_name})"

        # 布尔值转换
        if expression["value"] == "true":
            return "True"
        elif expression["value"] == "false":
            return "False"

        # 处理列表（数组初始化）
        elif isinstance(expression["value"], list):
            elements = [self.generate_expression({"value": elem}) for elem in expression["value"]]
            return f"[{', '.join(elements)}]"

        # 处理非字符串值
        elif not isinstance(expression["value"], str):
            node = expression["value"]
            if isinstance(node, dict) and node.get('node') == 'FunctionCall':
                code = self.generate_function_call(node)
                return code[0]
            else:
                return node.get('value', str(node))

        # 检查自增和自减运算符
        elif expression["value"].startswith("++") or expression["value"].startswith("--"):
            var = expression["value"][2:].strip()
            op = "+= 1" if expression["value"].startswith("++") else "-= 1"
            return f"{var} {op}"

        # 返回基础值
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
        elif statement["node"] == "Assignment":
            code.append(f"{statement['target']} = {self.generate_expression(statement['value'])}")
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
