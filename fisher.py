#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2019/5/4 10:37 PM
@Author  : sweetcs
@Site    : 
@File    : fisher.py
@Software: PyCharm
"""

from flask import Flask

app = Flask(__name__)


def hello():
    return "hello,征信指标"


app.add_url_rule("/hello/", view_func=hello)

app.config.from_object("config")

if __name__=='__main__':
    app.run(debug=app.config["DEBUG"], host=app.config["HOST"])