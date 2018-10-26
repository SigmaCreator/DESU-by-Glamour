import os
from terms import common_terms

phrase = [[]]   # The 1st column's the phrase, the other columns are the classifications for each word

def tokenize(text):

    os.system("rm output.txt")
    os.system("javac -encoding UTF-8 -cp POS_Tagging/kuromoji-0.7.7.jar POS_Tagging/POSTagger.java")
    os.system("java -Dfile.encoding=UTF-8 -cp POS_Tagging/kuromoji-0.7.7.jar:POS_Tagging POSTagger " + text + " >> output.txt")

def read_output():

    global phrase

    with open("output.txt","r") as file:
        content = file.readlines()

    content = [line.strip() for line in content]

    phrase = [[] for y in range(len(content))]

    for i in range(len(content)):
        
        piece = content[i].split("\t")          # Splits word and its classifications
        phrase[i].append(piece[0])              # Appends to the phrase matrix
        phrase[i].extend(piece[1].split(","))   # Extends the the row with the classifications

def interpret_output():
    pass

def main(text):

    tokenize(text)
    read_output()
    interpret_output()