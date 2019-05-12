#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2019/5/12 4:57 PM
@Author  : sweetcs
@Site    : 
@File    : helper.py
@Software: PyCharm
"""


def is_isbn_or_key(word):
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigtal():
        isbn_or_key = 'isbn'
    short_q = word.replace('-','')
    if '-' in word and len(short_q) == 10 and short_q.isdigtal():
        isbn_or_key = 'isbn'
    return isbn_or_key