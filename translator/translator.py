# main driver file that integrates everything

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from antlr4 import FileStream, CommonTokenStream
from parser.cpp_tinyLexer import cpp_tinyLexer
from parser.cpp_tinyParser import cpp_tinyParser
from translator.ast_generator import ASTGenerator
from translator.type_checker import TypeChecker
from translator.code_generator import CodeGenerator

def main(input_file):
    print(f"\n=== Starting translation of {input_file} ===")
    
    # Lexical and Syntax Analysis
    print("\n1. Performing Lexical and Syntax Analysis...")
    input_stream = FileStream(input_file)
    lexer = cpp_tinyLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = cpp_tinyParser(token_stream)
    parse_tree = parser.prog()
    
    # Debug: Print parse tree structure
    print("\nParse Tree Structure:")
    for child in parse_tree.children:
        print(f"Node type: {type(child)}")
        print(f"Text: {child.getText()}")
        print("---")
    
    print("   Parse tree generated successfully")

    # AST Generation
    print("\n2. Generating Abstract Syntax Tree...")
    ast_generator = ASTGenerator()
    ast = ast_generator.visit(parse_tree)
    
    if ast is None:
        print("   Error: AST generation returned None")
        return
    
    print("   AST generated successfully:")
    print(f"   {ast}")

    # Type Checking
    print("\n3. Performing Type Checking...")
    try:
        type_checker = TypeChecker()
        type_checker.check(ast)
        print("   Type checking passed")
    except TypeError as e:
        print(f"   Type Error: {str(e)}")
        return
    except Exception as e:
        print(f"   Unexpected error during type checking: {str(e)}")
        return

    # Code Generation
    print("\n4. Generating Python Code...")
    try:
        code_generator = CodeGenerator()
        python_code = code_generator.generate(ast)
        print("   Code generation completed")
    except Exception as e:
        print(f"   Error during code generation: {str(e)}")
        return

    # Output Python Code
    print("\n5. Writing Output File...")
    output_file = input_file.replace(".cpp", ".py")
    try:
        with open(output_file, "w") as f:
            f.write(python_code)
        print(f"   Successfully wrote Python code to {output_file}")
    except Exception as e:
        print(f"   Error writing to file: {str(e)}")
        return

    print("\n=== Translation completed successfully ===\n")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python translator.py <input_file.cpp>")
    else:
        main(sys.argv[1])
