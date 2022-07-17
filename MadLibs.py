#!/usr/bin/env python3

import re

print("Enter file name:")
fileName = input()
readFile = open(fileName, "r")
strFile = readFile.read()
readFile.close()
strRegex = re.compile(r"ADJECTIVE|NOUN|ADVERB|VERB")
words = strRegex.findall(strFile)
for word in words:
    if "AEIOU".find(word[0]) == -1:
        replace = input("Enter a " + word.lower() + ":\n")
    else:
        replace = input("Enter an " + word.lower() + ":\n")
    strFile = strRegex.sub(replace, strFile, count=1)
writeFile = open(fileName, "w")
writeFile.write(strFile)
writeFile.close()
