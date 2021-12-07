#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
微信公众号：AllTests软件测试
"""
import pytest
import allure
import logging
def func(abc):
    return abc + 1

def test_case3():
    assert func(3) == 5

class TestClass:
    def test_case1(self):
        x = "AllTests"
        assert "t" in x
        logging.info(x)

    def test_case2(self):
        y = "hello"
        assert "h" in y


