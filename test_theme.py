# -*- coding: utf-8 -*-

import unittest
from case.ThemeRelative import *


class test_theme(unittest.TestCase):

    def setUp(self):
        print("do something before test.Prepare environment.");

    def tearDown(self):
        print("do something after test.Clean up.")


    def test_favorTheme(self):
        print("获取收藏专题列表");
        favorTheme();

    def test_getFavorThemeList(self):
        print("获取相关专题");
        getFavorThemeList();

    def test_getRelativeTheme(self):
        print("获取相关专题");
        getRelativeTheme();

    def test_getThemeInfo(self):
        print("获取专题详情");
        getThemeInfo();


    def test_getThemeList(self):
        print("获取专题列表");
        getThemeList();
