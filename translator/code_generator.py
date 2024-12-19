# generate python code from the AST

class CodeGenerator:
    def generate(self, ast):
        code = []
        for node in ast:
            if node["node"] == "FunctionDefinition":
                code.append(f"def {node['name']}():")
                for statement in node["block"]:
                    if statement["node"] == "FunctionCall":
                        if(statement["name"] == "printf"):
                            code.append(f"    print({statement['arguments'][0]['value']})")
        return "\n".join(code)

    def generate_palindrome_check(self, input_string):
        return f"'{input_string}' == '{input_string}'[::-1]"

    def kmp_search(self, text, pattern):
        # Implement KMP algorithm here
        return "KMP search result"  # Placeholder for actual implementation
