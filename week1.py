def main():
    
    print("Input: ")
    sentence = input()
    print(alphabet_position(sentence))

def alphabet_position(sentence):
    sentence_Int = str()
    
    for c in sentence.lower():
        if(ord(c) >= 97 and ord(c) <= 122):
            sentence_Int += str(ord(c) % 96) + " "      
    return sentence_Int.strip()
            
if __name__ == "__main__":
    try:
        main()
    except:
        print("Error")
