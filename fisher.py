#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2019/5/4 10:37 PM
@Author  : sweetcs
@Site    : 
@File    : fisher.py
@Software: PyCharm
"""

from flask import Flask, make_response

app = Flask(__name__)


def hello():
    return "hello,征信指标"

def hello2bing():
    return "hello", 301, {"content-type":"text/plain","location":"https://wwww.bing.com"}

def hello2json():
    return "hello",200,{'content-type':'application/json'}

def hello2bing_with_make_response():
    headers={
        "content-type": "text/plain",
        "location": "https://wwww.bing.com"
    }
    return make_response("hello make response", 302, headers)

app.add_url_rule("/hello/", view_func=hello)
app.add_url_rule("/hello2bing/", view_func=hello2bing)
app.add_url_rule("/hello2json/", view_func=hello2json)
app.add_url_rule("/hello2bingv2/", view_func=hello2bing_with_make_response)

app.config.from_object("config")

if __name__=='__main__':
    app.run(debug=app.config["DEBUG"], host=app.config["HOST"], port=app.config["PORT"])