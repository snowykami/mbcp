# -*- coding: utf-8 -*-
"""
Copyright (C) 2020-2024 LiteyukiStudio. All Rights Reserved 

@Time    : 2024/8/26 上午6:58
@Author  : snowykami
@Email   : snowykami@outlook.com
@File    : test_question_1.py
@Software: PyCharm
"""
import logging

from mbcp.mp_math.vector import Vector3

from tests.answer import output_ans


class TestVector3:

    """测试问题集"""
    def test_vector_cross_product(self):
        """
        测试向量叉乘
        Returns:
        """
        v1 = Vector3(1, 2, 3)
        v2 = Vector3(3, 4, 5)
        actual_ans = v1.cross(v2)
        correct_ans = Vector3(-2, 4, -2)
        logging.info(f"正确答案{correct_ans}    实际答案{v1 @ v2}")

        assert correct_ans == actual_ans

    def test_determine_vector_parallel(self):
        """
        测试判断向量是否平行
        Returns:
        """
        """小题1"""
        correct_ans = True
        v1 = Vector3(1, 2, 3)
        v2 = Vector3(3, 6, 9)
        actual_ans = v1.is_parallel(v2)
        output_ans(correct_ans, actual_ans)
        assert correct_ans == actual_ans

        """小题2"""
        correct_ans = False
        v1 = Vector3(1, 2, 3)
        v2 = Vector3(3, 6, 8)
        actual_ans = v1.is_parallel(v2)
        output_ans(correct_ans, actual_ans)
        assert correct_ans == actual_ans



