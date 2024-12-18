# implements a basic symbol table for managing variables and their types

class SymbolTable:
    def __init__(self):
        self.table = {}
        self.scopes = [{}]  # Stack of scopes for nested blocks

    def enter_scope(self):
        self.scopes.append({})

    def exit_scope(self):
        self.scopes.pop()

    def add(self, name, symbol_type):
        if name in self.scopes[-1]:
            raise ValueError(f"Variable '{name}' already declared in this scope")
        self.scopes[-1][name] = symbol_type

    def lookup(self, name):
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
        raise ValueError(f"Variable '{name}' is not defined")

    def __str__(self):
        return str(self.scopes)
