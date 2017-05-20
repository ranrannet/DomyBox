# -*- coding: utf-8 -*-

import unittest

from case.HomeRecommend import getHomeRecommend
from case.user_action import favorCourse, praiseCourse


class test_user_action(unittest.TestCase):

    def setUp(self):
        print("do something before test.Prepare environment.");

    def tearDown(self):
        print("do something after test.Clean up.")


    def test_favorTheme(self):
        print("收藏专题");
        favorCourse();

    def test_praiseCourse(self):
        print("点赞");
        praiseCourse();


    def test_getHomeRecommend(self):
        print("获取首页banner");
        getHomeRecommend();