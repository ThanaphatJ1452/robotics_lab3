# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
sentence_Int = str()

def main():
    
    print("Input: ")
    sentence = input()
    convertToInt(sentence)

def alphabet_position(sentence):
    global sentence_Int
    
    for c in sentence.lower():
        if(ord(c) >= 97 and ord(c) <= 122):
            sentence_Int += str(ord(c) % 96) + " "      
    print(sentence_Int)
            
if __name__ == "__main__":
    try:
        main()
    except:
        print("Error")
