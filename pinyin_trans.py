#!/usr/bin/python
# -*- encoding: utf-8 -*-
# Maltego local transform for translating simplified Chinese character to Pinyin text
# This transfom makes use of Pypi module 'pinyin' (pip install pinyin)
import sys
import codecs
import pinyin
from MaltegoTransform import *

# Function to replace multiple chars in a string
def multiReplace(inputStr, replacements):
    # Iterate over the strings to be replaced
    for replaceStr in replacements:
        newStr = inputStr.replace(replaceStr, "") 
    return  newStr

# Function to clean input strings
def cleanInput(inputStr):
    cleanStr = multiReplace(inputStr, [',', '.', '-', "'"]).strip()
    return cleanStr

# Initialize Maltego library
m = MaltegoTransform()

# Handle and clean user input (simplified Chinese character string)
inputText = cleanInput(sys.argv[1].decode('utf8'))

# Tranlate input string into pinyin
translation = pinyin.get(inputText, format='strip', delimiter=' ')

# Add translation results as Maltego Phrase entity
m.addEntity('maltego.Phrase', translation)

# Return entity to Maltego chart
m.returnOutput()
