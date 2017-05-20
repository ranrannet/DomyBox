# -*- coding: utf-8 -*-

import unittest

from case.CourseWareRelative import afterWatchCourse, clearWatchHistory, getCoursewareInfo, getCoursewareList, \
    getWatchHistory



class test_course_ware(unittest.TestCase):

    def setUp(self):
        print("do something before test.Prepare environment.");

    def tearDown(self):
        print("do something after test.Clean up.")




    def test_afterWatchCourse(self):
        print("观看后上报观看行为");
        afterWatchCourse();

    def test_clearWatchHistory(self):
        print("清空观看历史");
        clearWatchHistory();

    def test_getCoursewareInfo(self):
        print("获取课件详情");
        getCoursewareInfo();

    def test_getCoursewareList(self):
        print("获取课件列表");
        getCoursewareList();

    def test_getWatchHistory(self):
        print("获取课件列表");
        getWatchHistory();


