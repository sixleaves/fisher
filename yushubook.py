#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2019/5/12 11:46 PM
@Author  : sweetcs
@Site    : 
@File    : yushubook.py
@Software: PyCharm
"""

from qunarhttp import QunarHttp

class YuShuBook:

    isbn_url = "http://t.yushu.im/v2/book/isbn/{}"
    keyword_url = "http://t.yushu.im/2/book/earch?q={}&start={}&count={}"

    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.isbn_url.format(isbn)
        result = QunarHttp.get(url)
        return result

    @classmethod
    def search_by_keyword(cls, keyword, start, count):
        url = cls.keyword_url.format(keyword, start, count)
        result = QunarHttp.get(url)
        return result