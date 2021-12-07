#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
微信公众号：AllTests软件测试
"""
import pytest

def setup_module():
    print("===== 整个.py模块开始前只执行一次 setup_module 例如:打开浏览器 =====")

def teardown_module():
    print("===== 整个.py模块结束后只执行一次 teardown_module 例如:关闭浏览器 =====")

def setup_function():
    print("===== 每个函数级别用例开始前都执行 setup_function =====")

def teardown_function():
    print("===== 每个函数级别用例结束后都执行 teardown_function =====")

def test_one():
    print("one")

def test_two():
    print("two")

class TestCase():
    def setup_class(self):
        print("===== 整个测试类开始前只执行一次 setup_class =====")

    def teardown_class(self):
        print("===== 整个测试类结束后只执行一次 teardown_class =====")

    def setup_method(self):
        print("===== 类里面每个用例执行前都会执行 setup_method =====")

    def teardown_method(self):
        print("===== 类里面每个用例结束后都会执行 teardown_method =====")

    def setup(self):
        print("===== 类里面每个用例执行前都会执行 setup =====")

    def teardown(self):
        print("===== 类里面每个用例结束后都会执行 teardown =====")

    def test_three(self):
        print("three")

    def test_four(self):
        print("four")

if __name__ == '__main__':
    pytest.main(["-q", "-s", "-ra", "test_setup_teardown.py"])