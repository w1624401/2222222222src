# To do : change str to char ; change comment initialization to # ;

import os
import sys
import lexering
import parsering
import objgen

def main():
    
    content  = ""           # This variable will hold the contents of the source code
    path     = os.getcwd()  # Holds path this script was executed from

    # Holds the name of the file the user wants to compile
    try:
        print("filename please:")
        fileName = input()
    except:
        print("[ERROR] Expected 1 Argument Containing File Name to be Run e.g 'tachyon main.c'")
        return

    # Check if the file extension is correct
    if fileName[len(fileName) - 2:len(fileName)] != ".c":
        print("[ERROR] File extension not recognised please make sure extension is '.c'")
        return # quit programme

    # Check to make sure that only one argument is passed
    try:
        print('[ERROR] Expected 1 argument found 2 (' + sys.argv[1] + ", " + sys.argv[2] + ')')
        return # quit programme
    except: pass

    # Open source code file and get it's content and save it to the 'contents' var
    try:
        with open(path + "/" + fileName, "r") as file:
            content = file.read()
    except: 
        print('Cannot find "' + fileName + '"')
    
    # --------------------------------------
    #  LEXER
    # --------------------------------------

    print('|||||||||||||||||||||  LEXER LOG  ||||||||||||||||||||| \n')
    # Create an instance of the lexer class
    lex = lexering.Lexer()

    # Call lexer method to perform lexical analysis on code
    tokens = lex.tokenize(content)
    print(tokens)
    print('\n||||||||||||||||||||||||||||||||||||||||||||||||||||||| \n')

    # --------------------------------------
    #  PARSER
    # --------------------------------------

    print('|||||||||||||||||||||  PARSER LOG  |||||||||||||||||||| \n')
    # Create an instance of the parser class
    Parser = parsering.Parser(tokens)

    # Call the parser method and pass in the tokens as arguments
    source_ast = Parser.parse(tokens)
    print(source_ast)
    print('\n||||||||||||||||||||||||||||||||||||||||||||||||||||||| \n')

    # --------------------------------------
    # Object Generation
    # --------------------------------------

    print('||||||||||||||||  OBJECT GENERATION LOG  ||||||||||||||| \n')
    # Create an instance of the Object Generator (objgen) class
    object_generator = objgen.ObjectGenerator(source_ast)

    # Call the object definer to get python exec() string
    exec_string = object_generator.object_definer(False)
    print('\n|||||||||||||||||||||||||||||||||||||||||||||||||||||||| \n')

    # Execute the tachyon code that has been transpiled to python code to get output
    print('|||||||||||||||||||  TRANSPILED CODE  |||||||||||||||||| \n')
    print(exec_string)
    print('\n|||||||||||||||||||||||||||||||||||||||||||||||||||||||| \n')

    print('|||||||||||||||||||||||  OUTPUT  ||||||||||||||||||||||| \n')
    exec(exec_string)
    print('\n|||||||||||||||||||||||||||||||||||||||||||||||||||||||| \n')

main()

