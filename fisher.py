#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2019/5/4 10:37 PM
@Author  : sweetcs
@Site    : 
@File    : fisher.py
@Software: PyCharm
"""
import json

from flask import Flask, make_response
from helper import is_isbn_or_key
from yushubook import YuShuBook

app = Flask(__name__)


def hello():
    return "hello,征信指标"

@app.route("/search/<q>/<page>")
def search(q, page):
    """
    q
    page
    :return:
    """
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
       result = YuShuBook.search_by_isbn(q)
    else:
       result = YuShuBook.search_by_keyword(q)
    # dict序列化,python自带的json库
    return json.dumps(result), 200, {'content-type':'application/json'}




app.config.from_object("config")

if __name__=='__main__':
    app.run(debug=app.config["DEBUG"], host=app.config["HOST"], port=app.config["PORT"])