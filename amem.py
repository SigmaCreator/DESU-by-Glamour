import os, grammar, log, translation
from terms import common_terms

phrase = [[]]   # The 1st column's the phrase, the other columns are the classifications for each word
translated = ""

def tokenize(text):

    with open("input.txt","w+",encoding='utf-8') as file : file.write(text)

    if os.name == 'nt' :

        os.system("javac -encoding UTF-8 -cp POS_Tagging/kuromoji-0.7.7.jar POS_Tagging/POSTagger.java")
        os.system("java -Dfile.encoding=UTF-8 -cp POS_Tagging/kuromoji-0.7.7.jar;POS_Tagging POSTagger > output.txt")

    if os.name == 'posix' :

        os.system("javac -encoding UTF-8 -cp POS_Tagging/kuromoji-0.7.7.jar POS_Tagging/POSTagger.java")
        os.system("java -Dfile.encoding=UTF-8 -cp POS_Tagging/kuromoji-0.7.7.jar:POS_Tagging POSTagger > output.txt")


def read_output():

    global phrase

    with open("output.txt","r",encoding='utf-8') as file : content = file.readlines()

    content = [line.strip() for line in content]

    phrase = [[] for y in range(len(content))]

    for i in range(len(content)) :
        
        piece = content[i].split("\t")          # Splits word and its classifications
        phrase[i].append(piece[0])              # Appends to the phrase matrix
        phrase[i].extend(piece[1].split(","))   # Extends the the row with the classifications

    for line in phrase : print(line)

def interpret_output():
    
    tokens = []
    words = []

    for i in range(len(phrase)):

        word = common_terms(phrase[i][0])
        first_token = common_terms(phrase[i][1])
        second_token = common_terms(phrase[i][2])
        base_form = common_terms(phrase[i][5])
        print(phrase[i][5])
        
        if (first_token == "PARTICLE") : tokens.append(word)

        elif (first_token == 'NOUN' and second_token == 'ADJ_NOUN') : tokens.append(second_token)
        
        elif ((word == 'NA' or word == 'DE') and first_token == 'AUX_VERB') : tokens.append(word)

        elif (word == "MASU") : log.set_verb_form("MASU") ; tokens.append(first_token)

        else : tokens.append(first_token)

        words.append(phrase[i][0])
    
    # print("Tokens - Before : ", tokens)

    grammar.token_wo_issho_ni_suru(tokens,words)
    
def translate(text):

    global translated

    translated = translation.translate(text,'pt')


def main(text):

    global translated

    tokenize(text)
    read_output()
    interpret_output()
    translate(text)
        

    return translated
