# -*- coding: utf-8 -*-
"""
Copyright (C) 2020-2024 LiteyukiStudio. All Rights Reserved 

@Time    : 2024/8/27 下午1:03
@Author  : snowykami
@Email   : snowykami@outlook.com
@File    : .answer.py
@Software: PyCharm
"""
from liteyuki.log import logger  # type: ignore


def output_answer(correct_ans, actual_ans, question: str = None):
    """
    输出答案
    Args:
        correct_ans:
        actual_ans:
        question:

    Returns:

    """
    print("")
    if question is not None:
        logger.info(f"问题：{question}")
    r = correct_ans == actual_ans
    if r:
        logger.success(f"测试正确    正确答案：{correct_ans}    实际答案：{actual_ans}")
    else:
        logger.error(f"测试错误    正确答案：{correct_ans}    实际答案：{actual_ans}")
