#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
微信公众号：AllTests软件测试
"""

import pytest

@pytest.fixture(params=["admin", "123456"])
def my_fixture(request):
    return request.param

@pytest.mark.parametrize("param1, param2", [("login", pytest.lazy_fixture("my_fixture"))])
def test_case(param1, param2):
    print("\n参数param1：" + param1)
    print("\n参数param2：" + param2)
    assert param2 in ["admin", "123456"]