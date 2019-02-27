#!/usr/bin/python
# -*- encoding: utf-8 -*-
# Maltego local tranform for the Baidu Translate API.
# Translate English to simplified Chinese.
import random
import codecs
import requests
import json
import md5
import urllib
from MaltegoTransform import *
import baiduApiKeys

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

# Handle and clean user input (English language text)
inputText = cleanInput((sys.argv[1]).decode('utf8'))

# Import Baidu API keys
appid = baiduApiKeys.appid
secretKey = baiduApiKeys.secretKey

# Configure required parameters for Baidu Translate API
baseurl = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
fromLang = 'en'
toLang = 'zh'
salt = random.randint(32768, 65536)
sign = appid + inputText.encode('utf8') + str(salt) + secretKey
m1 = md5.new()
m1.update(sign)
sign = m1.hexdigest()

# Create Baidu Translate API connection URL
url = '{}?appid={}&q={}&from={}&to={}&salt={}&sign={}'.format(baseurl, appid, urllib.quote(inputText.encode('utf8')), fromLang, toLang, str(salt), sign)

# Connect to Baidu Translate API using the created URL
try:
    # Baidu translate API get request
    r = requests.get(url)
    if r.status_code == 200:
        # Baidu translate API returns results in JSON array
        result = json.loads(r.content)
        translation = result['trans_result'][0]['dst']

        # Add translation results as Maltego Phrase entity
        m.addEntity('maltego.Phrase', translation.encode('utf8'))

except Exception as e:
    # Pass error message to Maltego UI
    m.addUIMessage("Source Language not Recognized.")

# Return results to Maltego chart
m.returnOutput()
