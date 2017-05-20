# coding: utf-8


import time

from util import ConvertObj
from util import HttpRequest
from util.UtilMethod import *;
from util.HttpRequest import *;

from vo.InGetCategorySubjects import InGetCategorySubjects;
from vo.InGetCourseCategories import InGetCourseCategories;
from vo.InGetCourseCount import InGetCourseCount;
from vo.InGetCourseInfo import InGetCourseInfo;
from vo.InGetCourseList import InGetCourseList;
from vo.InGetFavorCourseList import InGetFavorCourseList;
from vo.InGetFilterConditionList import InGetFilterConditionList;

from vo.InGetLearnedCourseList import InGetLearnedCourseList;
from vo.InGetThemeCourseList import InGetThemeCourseList;
from urllib import request

# 观看完成后上报观看行为
from vo.ResultObject import ResultObject

SORT = 1


class CourseRelative():

    # 获取分类下的科目
    def getCategorySubjects(self,category_id):
        url = "%sgetCategorySubjects" % config.API_ADDRESS;

        favorTheme = InGetCategorySubjects(config.API_KEY, config.USER_ID, category_id);
        from util import ConvertObj
        data = ConvertObj.convert_to_dict(favorTheme);
        from util import HttpRequest
        interface_result = HttpRequest.requestInterface(url, data);
        try:
            assert interface_result.result_status == config.INTERFACE_SUCCESS_STATUS, "接口请求失败";
            object = interface_result.error_reason;
            assert object['code'] == config.INTERFACE_SUCCESS_CODE, "接口返回码不正确";
            for favorTheme in object['data']:
                assert favorTheme["id"] is not None, "id 不能为空";
                assert favorTheme["name"] is not None, "科目名称不能为空";
                print(favorTheme['id']);
                print(favorTheme['name']);
            return object;
        except Exception as e:
            print(Exception, e);


            # 获取课程分类列表

    def getCourseCategories(self):
        url = "%sgetCourseCategories" % config.API_ADDRESS;
        object_vo = InGetCourseCategories(config.API_KEY);
        data = ConvertObj.convert_to_dict(object_vo);
        interface_result = HttpRequest.requestInterface(url, data);
        try:
            if interface_result.result_status == config.INTERFACE_SUCCESS_STATUS:
                object = interface_result.error_reason;

                for obj_detail in object['data']:
                    img_url = obj_detail['img_url'];
                    assert obj_detail['id'] is not None, "id不能为空";
                    assert obj_detail['name'] is not None, "name不能为空";
                    assert obj_detail['sort'] is not None, "排序不能为空";
                    assert obj_detail['img_url'] is not None, "分类图片不能为空";
                    img_url_http_code = get_url_isexist(img_url)
                    assert img_url_http_code == config.URL_SUCCESS_CODE, "分类图片地址不存在";


        except Exception as e:
            print(Exception, e);

    def getCourseCount(self):
        url = "%sgetCourseCount" % config.API_ADDRESS;

        favorTheme = InGetCourseCount(config.API_KEY, config.USER_ID, 1);

        data = ConvertObj.convert_to_dict(favorTheme);

        get_Favor_Theme_List = HttpRequest.requestInterface(url, data);

        assert get_Favor_Theme_List['code'] == config.INTERFACE_SUCCESS_CODE, "接口返回码错误";
        print(get_Favor_Theme_List['msg']);


        # 获取课程详情

    def getCourseInfo(self):
        url = "%sgetCourseInfo" % config.API_ADDRESS;
        favorTheme = InGetCourseInfo(config.API_KEY, config.USER_ID, 'HSNVC1281');

        data = ConvertObj.convert_to_dict(favorTheme);
        interface_result = HttpRequest.requestInterface(url, data);
        assert interface_result.result_status == config.INTERFACE_SUCCESS_STATUS, "接口返回码错误"
        object = interface_result.error_reason;

        for object_info in object['data']:
            assert object_info['id'] is not None, "ID不能为空";
            print(object_info['name']);
            assert object_info['share_url'] is not None, "分享的Url不能为空";
            from util.UtilMethod import get_url_isexist
            share_url_http_code = get_url_isexist(object_info['share_url'])
            assert share_url_http_code == config.URL_SUCCESS_CODE, "分享的地址不存在";

            assert object_info['subject_name'] is not None, "科目名称不能为空";
            assert object_info['subject_id'] is not None, "科目ID不能为空";
            assert object_info['category_id'] is not None, "分类ID不能为空";
            assert object_info['category_name'] is not None, "分类名称不能为空";
            assert object_info['praise_count'] is not None, "praise_count不能为空";
            assert object_info['watch_count'] is not None, "watch_count不能为空";
            assert object_info['organ_name'] is not None, "organ_name不能为空";
            assert object_info['img_url'] is not None, "img_url不能为空";
            assert object_info['organ_id'] is not None, "organ_id不能为空";
            assert object_info['name'] is not None, "name不能为空";
            assert object_info['name_us'] is not None, "name_us不能为空";
            assert object_info['summary'] is not None, "summary不能为空";

            assert object_info['img_url'] is not None, "img_url不能为空";
            img_url_http_code = get_url_isexist(object_info['img_url'])
            assert img_url_http_code == config.URL_SUCCESS_CODE, "课程图片地址不存在";

    def getCourseList(self):
        url = "%sgetCourseList" % config.API_ADDRESS;
        get_course_list = InGetCourseList(config.API_KEY, config.CATEGORY_ID, 'GS011', SORT);
        data = ConvertObj.convert_to_dict(get_course_list);
        interface_result = HttpRequest.requestInterface(url, data);
        assert interface_result.result_status == config.INTERFACE_SUCCESS_STATUS, "接口返回code错误"
        object = interface_result.error_reason;
        for course in object['data']:
            print(course['name']);
            print(course['id']);

            assert course['id'] is not None, "id 不能为空";
            assert course['name'] is not None, "课程名称不能为空";
            assert course['name_us'] is not None, "课程英文名称 不能为空";
            assert course['organ_id'] is not None, "组织机构ID 不能为空";
            assert course['organ_name'] is not None, "组织机构名称 不能为空";
            assert course['subject_id'] is not None, "科目ID 不能为空";
            assert course['subject_name'] is not None, "科目名称 不能为空";
            assert course['watch_count'] is not None, "观看数量 不能为空";
            assert course['favor_count'] is not None, "收藏数量 不能为空";
            assert course['img_url'] is not None, "图片地址 不能为空";
            from util.UtilMethod import get_url_isexist
            img_url_http_code = get_url_isexist(course['img_url'])
            assert img_url_http_code == config.URL_SUCCESS_CODE, "图片地址不存在";

            assert course['type'] is not None, "课程类型类型不能为空(课程类型1-普通课程，2-专题课程";
        return object;

    # 获取收藏的课程列表
    def getFavorCourseList(self):
        url = "%sgetFavorCourseList" % config.API_ADDRESS;

        favorTheme = InGetFavorCourseList(config.USER_ID, config.API_KEY, 0, 10);

        from util import ConvertObj
        data = ConvertObj.convert_to_dict(favorTheme);

        # get_Favor_Theme_List = HttpRequest.requestInterface(url, data);
        from util import HttpRequest
        interface_result = HttpRequest.requestInterface(url, data);
        assert interface_result.result_status == config.INTERFACE_SUCCESS_STATUS, "接口返回code错误"
        object = interface_result.error_reason;

        for favorTheme in object['data']:
            print(favorTheme['id']);
            print(favorTheme['name']);

            assert favorTheme['id'] is not None, "ID不能为空";
            assert favorTheme['subject_name'] is not None, "科目名称不能为空";
            assert favorTheme['subject_id'] is not None, "科目ID不能为空";
            assert favorTheme['category_id'] is not None, "分类ID不能为空";
            assert favorTheme['category_name'] is not None, "分类名称不能为空";
            assert favorTheme['organ_name'] is not None, "组织机构的ID不能为空";
            assert favorTheme['img_url'] is not None, "组织机构的ID不能为空";
            assert favorTheme['name'] is not None, "课程名称不能为空";
            assert favorTheme['summary'] is not None, "备注不能为空";

        return object;
            # print(favorTheme['condition_id']);
            # print(favorTheme['condition_name']);
            # print(favorTheme['label_id']);
            # print(favorTheme['label_name']);
            # print(favorTheme['praise_count']);
            # print(favorTheme['is_favor']);
            # print(favorTheme['is_praised']);
            # print(favorTheme['watch_count']);
            # print(favorTheme['speaker_id']);
            # print(favorTheme['speaker_name']);
            # print(favorTheme['img_url_us']);
            # print(favorTheme['type']);
            # print(favorTheme['uniq_id']);
            # print(favorTheme['organ_id']);
            # print(favorTheme['name']);
            # print(favorTheme['name_us']);
            # print(favorTheme['summary']);
            # print(favorTheme['status']);
            # print(favorTheme['update_status']);


            # 获取课程分类列表

        def getFilterConditionList(self):
            url = "%sgetFilterConditionList" % config.API_ADDRESS;

            favorTheme = InGetFilterConditionList(config.API_KEY, 'HSNVC326', config.USER_ID, 1);

            data = ConvertObj.convert_to_dict(favorTheme);

            get_Favor_Theme_List = HttpRequest.requestInterface(url, data);

            print(get_Favor_Theme_List);
            print(get_Favor_Theme_List['code']);
            print(get_Favor_Theme_List['msg']);


            # 获取已学完未学完的课程列表

    def getLearnedCourseList(self):
        url = "%sgetLearnedCourseList" % config.API_ADDRESS;
        favorTheme = InGetLearnedCourseList(config.API_KEY, 'TH113', 10265093, 0, 0, 10000);
        data = ConvertObj.convert_to_dict(favorTheme);
        interface_result = HttpRequest.requestInterface(url, data);
        assert interface_result.result_status == config.INTERFACE_SUCCESS_STATUS, "接口返回码错误";
        object = interface_result.error_reason;
        for object_info in object['data']:
            assert object_info['id'] is not None, "id不能为空";
            assert object_info['name'] is not None, "name 不能为空";
            assert object_info['name_us'] is not None, "name_us 不能为空";
            assert object_info['img_url'] is not None, "img_url 不能为空";
            assert object_info['courseware_total_count'] is not None, "课件总数量不正常";
            assert object_info['courseware_finished_count'] is not None, "courseware_finished_count 不能为空";
            assert object_info['courseware_total_count'] is not None, "课件总数量不正常";
            assert object_info['type'] is not None, "type不能为空";

    def getThemeCourseList(self):
        url = "%sgetThemeCourseList" % config.API_ADDRESS;

        favorTheme = InGetThemeCourseList(config.API_KEY, 'TH113');

        data = ConvertObj.convert_to_dict(favorTheme);

        interface_result = HttpRequest.requestInterface(url, data);

        assert interface_result.result_status == config.INTERFACE_SUCCESS_STATUS, "接口返回码错误"
        object = interface_result.error_reason;
        assert object['code'] == config.INTERFACE_SUCCESS_CODE, "获取专题的课程列表失败";

        # for favorTheme in interface_result['data']:
        #     print(favorTheme['id']);
        #     print(favorTheme['name']);
        #     print(favorTheme['name_us']);
        #     print(favorTheme['img_url']);
        #     print(favorTheme['type']);
        #     print(favorTheme['img_url_us']);
