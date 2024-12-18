# generate python code from the AST

class CodeGenerator:
    def generate(self, ast):
        code = []
        for node in ast:
            if node["node"] == "PalindromeCheck":
                code.append(f"print({self.generate_palindrome_check(node['input'])})")
            elif node["node"] == "SortList":
                code.append(f"print(sorted([{', '.join(node['items'])}]))")
            elif node["node"] == "KMPMatch":
                code.append(f"print(self.kmp_search('{node['text']}', '{node['pattern']}'))")
            elif node["node"] == "ArithmeticExpression":
                code.append(f"print({node['expression']})")
        return "\n".join(code)

    def generate_palindrome_check(self, input_string):
        return f"'{input_string}' == '{input_string}'[::-1]"

    def kmp_search(self, text, pattern):
        # Implement KMP algorithm here
        return "KMP search result"  # Placeholder for actual implementation
