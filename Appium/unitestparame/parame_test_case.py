# coding = utf-8
"""
@All-project: Appium
@author: ZWNONG
@file: parame_test_case.py
@time: 2020-06-23 15:39:13
"""
import unittest


class ParameTestCase(unittest.TestCase):
    def __init__(self, methodName='runTest', parame=None):
        super(ParameTestCase, self).__init__(methodName)
        global parames
        parames = parame
