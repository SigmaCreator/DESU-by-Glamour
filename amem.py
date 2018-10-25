import os, sys

text = sys.argv[1]

os.system("rm output.txt")
os.system("java -Dfile.encoding=UTF-8 -cp POS_Tagging/kuromoji-0.7.7.jar:POS_Tagging POSTagger " + text + " >> output.txt")

with open("output.txt","r") as file:
    content = file.readlines()

content = [line.strip() for line in content]

phrase = [[] for y in range(len(content))]

for i in range(len(content)):
    
    first = content[i].split("\t")
    phrase[i].append(first[0])
    phrase[i].extend(first[1].split(","))

for line in phrase:
    print(line)



