# -*- coding: utf-8 -*-

import unittest

from case.CourseRelative import getCategorySubjects, getCourseCategories, getCourseInfo, getFavorCourseList, \
    getCourseList, getThemeCourseList, getLearnedCourseList
from case.CourseWareRelative import afterWatchCourse, clearWatchHistory, getCoursewareInfo, getCoursewareList, \
    getWatchHistory
from case.user_action import favorCourse, praiseCourse
from case.ThemeRelative import *


class test_course(unittest.TestCase):
    def setUp(self):
        print("do something before test.Prepare environment.");

    def tearDown(self):
        print("do something after test.Clean up.")

    def test_getCategorySubjects(self):
        print("获取一个分类下的科目列表");
        getCategorySubjects();

    def test_getCourseCategories(self):
        print("获取课程分类列表");
        getCourseCategories();


    def test_getCourseInfo(self):
        print("获取课程详情");
        getCourseInfo();

    def test_getCourseList(self):
        print("获取课程列表");
        getCourseList();


    def test_getFavorCourseList(self):
        print("获取课收藏的课程列表");
        getFavorCourseList();

    def test_getLearnedCourseList(self):
        print("获取已学完未学完的课程列表");
        getLearnedCourseList();

    def test_getThemeCourseList(self):
        print("获取一个专题的课程列表");
        getThemeCourseList();







