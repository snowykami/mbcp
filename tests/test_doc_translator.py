# -*- coding: utf-8 -*-
"""
Copyright (C) 2020-2024 LiteyukiStudio. All Rights Reserved 

@Time    : 2024/8/29 下午12:06
@Author  : snowykami
@Email   : snowykami@outlook.com
@File    : test_doc_translator.py
@Software: PyCharm
"""

from litedoc.translator import translate


def test():
    print(translate("Hello, world!", "Chinese", "English"))
