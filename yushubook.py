#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2019/5/12 11:46 PM
@Author  : sweetcs
@Site    : 
@File    : yushubook.py
@Software: PyCharm
"""

from http import Http

class YuShuBook:

    isbn_url = "http://t.yushu.im/v2/book/isbn/{}"
    keyword_url = "http://t.yushu.im/2/book/earch?q={}&start={}&count={}"

    def search_by_isbn(cls, isbn):
        url = cls.isbn_url.format(isbn)
        result = Http.get(url)
        return result

    def search_by_keyword(cls, keyword, start, count):
        url = cls.keyword_url.format(keyword, start, count)
        result = Http.get(url)
        return result