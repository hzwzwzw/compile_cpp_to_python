# perform type checking on AST

from translator.symbol_table import SymbolTable

class TypeChecker:
    def __init__(self):
        self.symbol_table = SymbolTable()

    def check(self, ast):
        for node in ast:
            if node["node"] == "VariableDeclaration":
                self.symbol_table.add(node["name"], node["type"])
            elif node["node"] == "VariableDefinition":
                declared_type = self.symbol_table.lookup(node["name"])
                if declared_type not in ["int", "float"]:  # Simplified type check
                    raise TypeError(f"Invalid type assignment to '{node['name']}'")
            elif node["node"] == "PalindromeCheck":
                # Add any specific checks for palindrome input if necessary
                pass
            elif node["node"] == "SortList":
                # Add any specific checks for sorting input if necessary
                pass
            elif node["node"] == "KMPMatch":
                # Add any specific checks for KMP matching if necessary
                pass
            elif node["node"] == "ArithmeticExpression":
                # Add any specific checks for arithmetic expressions if necessary
                pass
        print("Type check passed.")
