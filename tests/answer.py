# -*- coding: utf-8 -*-
"""
Copyright (C) 2020-2024 LiteyukiStudio. All Rights Reserved 

@Time    : 2024/8/27 下午1:03
@Author  : snowykami
@Email   : snowykami@outlook.com
@File    : .answer.py
@Software: PyCharm
"""
from typing import Optional

from liteyuki.log import logger  # type: ignore


def output_ans(correct_ans, actual_ans, condition: Optional[bool] = None,question: Optional[str] = None):
    """
    输出答案
    Args:
        correct_ans:
        actual_ans:
        condition: 判对条件
        question: 问题

    Returns:

    """
    print("")
    if question is not None:
        logger.info(f"问题：{question}")
    r = (correct_ans == actual_ans) if condition is None else condition
    if r:
        logger.success(f"测试正确    正确答案：{correct_ans}    实际答案：{actual_ans}")
    else:
        logger.error(f"测试错误    正确答案：{correct_ans}    实际答案：{actual_ans}")
        assert r


def output_step_ans(correct_ans, actual_ans, condition: Optional[bool] = None, question: Optional[str] = None):
    """
    输出步骤答案
    Args:
        correct_ans: 正确答案
        actual_ans: 实际答案
        condition: 判对条件
        question: 问题

    Returns:

    """
    print("")
    if question is not None:
        logger.info(f"  步骤：{question}")
    r = (correct_ans == actual_ans) if condition is None else condition
    if r:
        logger.success(f"  正确    正确：{correct_ans}    实际：{actual_ans}")
    else:
        logger.error(f"  错误    正确：{correct_ans}    实际：{actual_ans}")
