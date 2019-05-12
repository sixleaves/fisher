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

@app.route("/search/<q>/<page>")
def search(q, page):
    """
    q
    page
    :return:
    """
    isbn_or_key = 'key'
    if len(q) == 13 and q.isdigtal():
        isbn_or_key = 'isbn'
    short_q = q.replace('-','')
    if '-' in q and len(short_q) == 10 and short_q.isdigtal():
        isbn_or_key = 'isbn'
    pass




app.config.from_object("config")

if __name__=='__main__':
    app.run(debug=app.config["DEBUG"], host=app.config["HOST"], port=app.config["PORT"])