# Maltego Chinese Language Transforms

A set of three maltego local transforms useful for handling and translating Chinese character strings. The three transforms can offer the following options when assigned as local transforms to various entities in Maltego:

- Translate Simplified Chinese characters to English
- Translate English to Simplified Chinese characters
- Translate Simplified Chinese character to Pinyin.

I frequently use Chinese language data sources within Maltego charts. For example, data sourced from Weibo, web scrapes, forums, bbs and even Chinese language entries in WHOIS records. I thought it useful to have a simple set of machine translation transforms at my fingertips within Maltego as i'm building my charts.  

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

![Example of transforms in action](/doc/translate.png)

### Prerequisites

The transforms are written in Python 2.7.

[Baidu's Fanyi](http://api.fanyi.baidu.com) translation API is used to translate between Simplified Chinese and English and vice versa. 

A fantastic Python module *pinyin* is used to translate Simplified characters to Pinyin. [Read more here](http://pinyin.lxyu.net/)

You'll need the following Python modules installed too if you don't already have them:

```
import requests
import json
import md5
import urllib
```
and

```
import MaltegoTransform
```

This last module import is the Maltego python transform library. You can grab a copy from the [Maltego developer site](https://docs.maltego.com/helpdesk/attachments/2015007304961). 

### Installing

You'll need to sign up to Baidu's services in order to set up an APP and obtain credentials for use with the translation API. Unless translating large volumes of text, the free tier offering is usually generous enough. 

Place your Baidu APP ID and API Key in the *baiduApiKey.py* file. 

The *pinyin* module is available from PyPI and can easily be installed as follows:

```
pip install pinyin
```

Configure the local transforms in Maltego, [see the Configuration Guide](https://docs.maltego.com/support/solutions/articles/15000010781-local-transforms). In short, you'll need to link the transforms to specific entity types and point Maltego to both your local Python installation and your local copy of these transform scripts. 

## Running the Transforms

These transforms can be run like any other local transforms. I find it useful to add all three into a Maltego *Transform Set* named "Translation", making it easier to group and locate them all in one place on Maltego menus. 

## Built With

* [Python](http://www.python.org)
* [Maltego Local Python Library](https://docs.maltego.com/support/solutions/articles/15000019558-python-local-library-reference)

## Authors

* **Andrew Houlbrook** - *Initial work* - [ba2baha3o](https://github.com/ba2baha3o)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details