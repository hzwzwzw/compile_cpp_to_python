import sys
import os
import json
from antlr4 import *
from antlr4.tree.Trees import Trees
from cpp_tinyLexer import cpp_tinyLexer
from cpp_tinyParser import cpp_tinyParser

def parse_file(file_name):
    input_stream = FileStream(file_name)
    lexer = cpp_tinyLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = cpp_tinyParser(stream)
    tree = parser.prog()

    return tree

def tree_to_json(tree, parser):
    def _tree_to_json(node):
        if node.getChildCount() == 0:
            return {"text": node.getText()}#, "type": parser.ruleNames[node.getRuleIndex()]}
        else:
            children = []
            for child in node.getChildren():
                children.append(_tree_to_json(child))
            return {"type": parser.ruleNames[node.getRuleIndex()], "children": children}
    return json.dumps(_tree_to_json(tree), indent=4)

def proc(file_name):
    dir_name = os.path.dirname(file_name)
    tree = parse_file(file_name)
    parser = cpp_tinyParser(CommonTokenStream(cpp_tinyLexer(FileStream(file_name))))
    tree_json = tree_to_json(tree, parser)
    # to file
    print(tree_json)
    with open(file_name.replace(".cpp", "") + ".json", "w") as f:
        f.write(tree_json)


if __name__ == "__main__":
    # file_name = input("Enter the file name to parse: ")
    filename = {
        "../example/test0.cpp",
        "../example/test1.cpp",
        "../example/test2.cpp",
        "../example/test3.cpp"
    }
    for file_name in filename:
        proc(file_name)
    