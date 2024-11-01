import sys
import os
import json
from antlr4 import *
from antlr4.tree.Trees import Trees
from cpp_tinyLexer import cpp_tinyLexer
from cpp_tinyParser import cpp_tinyParser
def generate_token_stream(file_name):
    input_stream = FileStream(file_name, encoding='utf-8')
    lexer = cpp_tinyLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()
    tokens = token_stream.getTokens(0, token_stream.getNumberOfOnChannelTokens() - 1)
    
    token_list = []
    for token in tokens:
        token_type = lexer.symbolicNames[token.type]
        token_value = token.text
        token_list.append(f"{token_type}: {token_value}")
    
    return token_list

def proc(file_name):
    tokens = generate_token_stream(file_name)
    for token in tokens:
        print(token)
    with open(file_name.replace(".cpp", "") + "_tokens.txt", 'w', encoding='utf-8') as f:
        for token in tokens:
            f.write(token + '\n')


if __name__ == "__main__":
    # file_name = input("Enter the file name to parse: ")
    filename = {
        # "C:\\Users\\23576\\Desktop\\汇编与编译原理\\final\\example\\test0.cpp"
        "../example/test0.cpp",
        "../example/test1.cpp",
        "../example/test2.cpp",
        "../example/test3.cpp",
        "../example/test4.cpp"
    }
    for file_name in filename:
        proc(file_name)
    