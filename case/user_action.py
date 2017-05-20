# coding: utf-8


from util import ConvertObj
from util import HttpRequest
from util import config
import unittest
from vo.InFavorCourse import InFavorCourse;
from vo.InPraiseCourse import InPraiseCourse;
from vo.ResultObject import ResultObject;
from vo.InRemoveUserFavorCourse import InRemoveUserFavorCourse;
from case.CourseRelative import CourseRelative


class user_action(unittest.TestCase):
    def setUp(self):
        print("in......")

    # 获取收藏课程列表
    def test_get_favor_course_list(self):
        obj = CourseRelative.getFavorCourseList(self);

    # 收藏课程
    def test_favorCourse(self):
        url = "%sfavorCourse" % config.API_ADDRESS;
        favorTheme = InFavorCourse(config.IDS, config.USER_ID, config.API_KEY);
        data = ConvertObj.convert_to_dict(favorTheme);
        interface_result = HttpRequest.requestInterface(url, data);

        assert interface_result.result_status == config.INTERFACE_SUCCESS_STATUS, "接口返回码错误";
        object = interface_result.error_reason;
        assert object['code'] == config.INTERFACE_SUCCESS_CODE, "接口返回码错误";
        for object_info in object['data']:
            assert object_info['count'] is not None, "攒点数量有误";
        # 查看收藏的课程
        object = CourseRelative.getFavorCourseList(self);
        for favorTheme in object['data']:
            # print(favorTheme['id']);
            if config.IDS == favorTheme['id']:
                print("------true-------------")

    # 取消收藏
    def test_remove_user_collection(self):
        url = "%sremoveUserFavorCourse/%s/%s/%s" % (
            config.API_ADDRESS, config.CATEGORY_TYPE, config.TYPE, config.IDS);
        inputParam = InRemoveUserFavorCourse(config.API_KEY, config.USER_ID);
        data = ConvertObj.convert_to_dict(inputParam);
        interface_result = HttpRequest.requestInterface(url, data)
        assert interface_result.result_status == config.INTERFACE_SUCCESS_STATUS, "接口返回码错误";
        object = interface_result.error_reason;
        code = object['code'];
        print(code);
        assert code == config.INTERFACE_SUCCESS_CODE, "清除用户历史记录失败"
        print("----------------------------------")
        object = CourseRelative.getFavorCourseList(self);

        for favorTheme in object['data']:
            # print(favorTheme['id']);
            if config.IDS == favorTheme['id']:
                print("------false-------------")


    # 点赞
    def test_praiseCourse(self):
        url = "%spraiseCourse" % config.API_ADDRESS;
        favorTheme = InPraiseCourse(config.IDS, config.USER_ID, config.REGISTER_ID, config.API_KEY);
        data = ConvertObj.convert_to_dict(favorTheme);
        interface_result = HttpRequest.requestInterface(url, data);
        assert interface_result.result_status == config.INTERFACE_SUCCESS_STATUS, "接口返回码错误";
        object = interface_result.error_reason;
        for object_info in object['data']:
            assert object_info['count'] is not None, "点赞数量没有增加";




    def tearDown(self):
        print("end.........")
