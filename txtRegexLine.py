#!/usr/bin/env python3

import os
import re

dirName = input("Enter a dirctory name:\n") 
if os.path.isdir(dirName) == False:
    print("This folder does not exist.")
    exit(1)
regexExp = input("Enter an regex expersion:\n")
regexPattern = re.compile(r"%s" % regexExp)
for fileName in os.listdir(dirName):
    if os.path.isfile(fileName) == False:
        continue
    file_ = open(fileName, "r")
    for line in file_.readlines():
        if re.match(regexPattern, line) != None:
            print(line)