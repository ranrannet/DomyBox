# coding: utf-8

# import urllib2

from util import ConvertObj
from util import HttpRequest
from util import config
from util.UtilMethod import get_url_isexist
from vo.InGetCoursewareInfo import InGetCoursewareInfo

from vo.ResultObject import ResultObject

from vo.InAfterWatchCourse import InAfterWatchCourse;
from vo.InClearWatchHistory import InClearWatchHistory;
from vo.InGetCoursewareList import InGetCoursewareList;
from vo.InGetWatchHistory import InGetWatchHistory;

class CourseWareRelative():

    # 观看完成后上报观看行为
    def afterWatchCourse(self):
        url = "%safterWatchCourse" % config.API_ADDRESS;
        favorTheme = InAfterWatchCourse(config.API_KEY, 10599667, 'HSNVC326', 'HSNCV7489', 8, 0, 1, 1,
                                        'DBA30104150100260');
        data = ConvertObj.convert_to_dict(favorTheme);
        interface_result = HttpRequest.requestInterface(url, data);
        assert interface_result.result_status == config.INTERFACE_SUCCESS_STATUS, "接口返回码错误";
        object = interface_result.error_reason;
        assert object['code'] is not None, "上报观看行为失败";


    def clearWatchHistory(self):
        url = "%sclearWatchHistory" % config.API_ADDRESS;
        favorTheme = InClearWatchHistory(config.API_KEY, 10599667);
        data = ConvertObj.convert_to_dict(favorTheme);
        interface_result = HttpRequest.requestInterface(url, data);
        try:
            assert interface_result.result_status == config.INTERFACE_SUCCESS_STATUS, "接口返回码错误";
            object = interface_result.error_reason;
            assert object["code"] == config.INTERFACE_SUCCESS_CODE, "清空观看历史，清除失败";

        except Exception as e:
            print(Exception, "---------------Exception----------:", e);  # # 获取课件详情


    def getCoursewareInfo(self):
        url = "%sgetCoursewareInfo" % config.API_ADDRESS;
        favorTheme = InGetCoursewareInfo(config.API_KEY, config.USER_ID, "HSNVC326", 'HSNCV7489', 8, 0, 1, 1, 1);
        data = ConvertObj.convert_to_dict(favorTheme);
        try:
            interface_result = HttpRequest.requestInterface(url, data);
            assert interface_result.result_status == config.INTERFACE_SUCCESS_STATUS, "接口返回码错误"
            object = interface_result.error_reason;

            for object_info in object['data']:
                assert object_info['fhd_url'] is not None, "fhd_url地址不能为空";
                assert object_info['hd_url'] is not None, "hd_url地址不能为空";
                assert object_info['sd_url'] is not None, "sd_url地址不能为空";
                assert object_info['ld_url'] is not None, "ld_url地址不能为空";
                assert object_info['id'] is not None, "id地址不能为空";

                img_url_http_code = get_url_isexist(object_info['fhd_url'])
                assert img_url_http_code == config.URL_SUCCESS_CODE, "fhd_url地址不存在";

                img_url_http_code = get_url_isexist(object_info['hd_url'])
                assert img_url_http_code == config.URL_SUCCESS_CODE, "hd_url地址不存在";

                img_url_http_code = get_url_isexist(object_info['sd_url'])
                assert img_url_http_code == config.URL_SUCCESS_CODE, "sd_url地址不存在";

                img_url_http_code = get_url_isexist(object_info['ld_url'])
                assert img_url_http_code == config.URL_SUCCESS_CODE, "ld_url地址不存在";


        except Exception as e:
            print(Exception, "----Exception-------------------:", e);  # # 获取课件列表


    def getCoursewareList(self):
        url = "%sgetCoursewareList" % config.API_ADDRESS;
        course_list = InGetCoursewareList(config.API_KEY, 'HSNVC1272', 10599667, 0, 0, 10000);
        data = ConvertObj.convert_to_dict(course_list);
        interface_result = HttpRequest.requestInterface(url, data);
        try:
            assert interface_result.result_status == config.INTERFACE_SUCCESS_STATUS, "接口返回码错误";
            object = interface_result.error_reason;
            for data_info in object['data']:
                print(data_info['name'])
                assert data_info['name'] is not None, "课件名称不能为空";
                # assert data_info['name_us'] is not None, "课件英文名称不能为空";
                assert data_info['id'] is not None, "课件ID不能为空";

        except Exception as e:
            print(Exception, ":------getCoursewareList---------------", e);  # 获取观看历史


    def getWatchHistory(self):
        url = "%sgetWatchHistory" % config.API_ADDRESS;
        favorTheme = InGetWatchHistory(config.API_KEY, 10599667);  # 将对象转成字典
        data = ConvertObj.convert_to_dict(favorTheme);

        interface_result = HttpRequest.requestInterface(url, data);
        assert interface_result.result_status == config.INTERFACE_SUCCESS_STATUS, "接口请求失败";
        object = interface_result.error_reason;
        for favorTheme in object['data']:
            assert favorTheme['id'] is not None, "id不能为空";
            assert favorTheme['courseware_id'] is not None, "课件id不能为空";
            assert favorTheme['name'] is not None, "课程名称不能为空";
            assert favorTheme['name_us'] is not None, "课程英文名称不能为空";
            assert favorTheme['img_url'] is not None, "图片地址不能为空";
            assert favorTheme['courseware_name'] is not None, "课件名称不能为空";
            assert favorTheme['type'] is not None, "类型不能为空";
            assert favorTheme['view_type'] is not None, "view_type不能为空";
            assert favorTheme['status'] is not None, "状态不能为空";
