#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2019/5/12 11:25 PM
@Author  : sweetcs
@Site    : 
@File    : qunarhttp.py
@Software: PyCharm
"""
import requests


class QunarHttp:

    @staticmethod
    def get(url, return_json=True):

        r = requests.get(url)

        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text
