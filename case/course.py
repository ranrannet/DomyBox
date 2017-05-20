# coding=utf-8
import os
import unittest
from case.identity import identity
from case.CourseRelative import CourseRelative
from case.CourseWareRelative import CourseWareRelative


class course(unittest.TestCase):
    def setUp(self):
        print("in......")


    # 用户未选择身份流程（2）
    def test_get_vip_course_categories(self):
        # 获取身份列表
        # identity.get_identity_List(self);
        # 设置身份（一级身份少儿、二级身份0-2岁）
        # identity.get_vip_course_categories(self);
        # 获取科目列表
        # CourseRelative.getCategorySubjects(self,1);
        # 获取科目下对应的课程
        # CourseRelative.getCourseList(self);
        # CourseRelative.getCourseInfo(self);
         CourseWareRelative.getCoursewareList(self);
    def tearDown(self):
        print("end.........")
