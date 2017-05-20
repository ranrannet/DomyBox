# -*- coding: utf-8 -*-

import unittest
from case.ThemeRelative import *
from vo.IngetIdentityList import InGetIdentityList


class test_identity(unittest.TestCase):

    def setUp(self):
        print("do something before test.Prepare environment.");

    def tearDown(self):
        print("do something after test.Clean up.")

    def test_getIdentityList(self):
       print("1111");
