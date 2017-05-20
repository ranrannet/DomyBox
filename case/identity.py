# coding=utf-8
import os
import unittest

from selenium import webdriver

from connectdb.test_sql import test_sql
from util import ConvertObj
from util import HttpRequest
from util import UtilMethod
from util import config
from vo.INGetNewHomeRecommend import INGetNewHomeRecommend
from vo.InClearWatchHistory import InClearWatchHistory
from vo.InGetActivityPermission import InGetActivityPermission
from vo.InGetCategoryCourseList import InGetCategoryCourseList
from vo.InGetRecommendList import InGetRecommendList
from vo.InGetUserVip7Config import InGetUserVip7Config
from vo.InGetVipCourseCategories import InGetVipCourseCategories
from vo.InPlaySettings import InPlaySettings
from vo.InUpdateUserIdentity import InUpdateUserIdentity
from vo.IngetIdentityList import InGetIdentityList
# 课程详情
from vo.getUserIdentity import InGetUserIdentity
from util.UtilMethod import get_url_isexist

# channel:访问终端是什么,(1=tv,2=pc,3=android,4=ios);默认为1
CHANNEL = 0
TYPE = 1
CONTENT_ID = 1
PAGE_SIZE = 10
PAGE_NUMBER = 0
COURSE_TYPE = 1


PARENT_IDENTITY_ID = 4;
CHANNEL = "1";
# selectType:身份的选择方式，0=选择的默认身份,1=手动设置；默认为0
SELECT_TYPE = "0";
# identity:身份二级Id
IDENTITY_ID = 39;


class identity():
    # def setUp(self):
    #     print("in......")
    #


    # 获取身份字典数据列表

    def get_identity_List(self):
        url = "%sidentity/getIdentityList/%s/%s" % (config.API_ADDRESS, "0", "2");
        favorTheme = InGetIdentityList(config.API_KEY);
        data = ConvertObj.convert_to_dict(favorTheme);
        interface_result = HttpRequest.requestInterface(url, data)
        assert interface_result.result_status == config.INTERFACE_SUCCESS_STATUS, "接口返回码错误";
        object = interface_result.error_reason;

        for object_info in object['data']:
            print("一级身份id：" + str(object_info['identityId']));

            print("一级身份名称：" + object_info['identityName']);
            assert object_info['identityId'] is not None, "身份ID不能为空";
            assert object_info['identityName'] is not None, "身份ID不能为空";
            url_http_code = UtilMethod.get_url_isexist(object_info['identityImgUrl']);
            assert url_http_code == config.URL_SUCCESS_CODE, "身份图片不存在";

            print(object_info['indexPosition']);
            i = 0;
            for sub_obj in object_info["childList"]:
                sub_identity = test_sql.test_get_sub_identity(self, object_info['identityId'], i);
                true_identity_id = sub_identity['id'];
                true_identity_name = sub_identity['name'];
                print("---true------", true_identity_id, "---------", true_identity_name)
                print("---now------", sub_obj['identityId'], "---------", sub_obj['identityName']);

                assert true_identity_id == sub_obj['identityId'], "子身份id不一致";
                assert true_identity_name == sub_obj['identityName'], "子身份name不一致";
                i = i + 1;

    # 获取用户身份
    def getUserIdentity(self):
        url = "%sidentity/getUserIdentity" % (config.API_ADDRESS);
        inputParam = InGetUserIdentity(config.API_KEY, config.USER_ID);
        data = ConvertObj.convert_to_dict(inputParam);
        interface_result = HttpRequest.requestInterface(url, data)
        assert interface_result.result_status == config.INTERFACE_SUCCESS_STATUS, "接口返回码错误";
        object = interface_result.error_reason;
        data_info = object["data"];
        print(data_info['existsIdentity']);
        print(data_info['identityId']);

        print(data_info['parentIdentityImgUrl']);
        assert data_info['parentIdentityImgUrl'] is not None, "图片地址不存在"

        identity_pic = get_url_isexist(data_info['parentIdentityImgUrl'])
        assert identity_pic == config.URL_SUCCESS_CODE, "身份图片不存在";

        print(data_info['parentIdentityName']);
        assert data_info['parentIdentityName'] is not None, "父级身份名称不能为空"

        print(data_info['identityName']);
        assert data_info['identityName'] is not None, "子级身份名称不能为空"

        print(data_info['parentIdentityId']);
        assert data_info['parentIdentityId'] is not None, "父级身份ID不能为空"

        return object;

        # 获取用户当前的身份数据
        # "select sub.`name` as 'identityName',par.`name` as 'parentIdentityName',sub.id as 'parentIdentityId',par.id as 'identityId' from user_identity ui left join identity sub on ui.parent_identity_id = sub.id left join identity par on ui.identity_id = par.id where ui.user_id=11394580 and ui.status =1;"

    # 获取自动播放视频的状态
    def test_get_video_autoplay(self):
        url = "%sconfig/getActivityPermission/autoplay" % (config.API_ADDRESS);
        inputParam = InGetActivityPermission(config.API_KEY);
        data = ConvertObj.convert_to_dict(inputParam);
        interface_result = HttpRequest.requestInterface(url, data)
        assert interface_result.result_status == config.INTERFACE_SUCCESS_STATUS, "接口返回码错误";
        object = interface_result.error_reason;
        data_info = object["data"];
        print(data_info['confValue']);
        assert data_info['confValue'] is not None, "开关value不能为空"

        print(data_info['confKey']);
        assert data_info['confKey'] is not None, "开关key不能为空"

        print(data_info['description']);
        assert data_info['description'] is not None, "描述不能为空"

    # 获取是否可以领取7天VIP 11394580
    def test_getUserVip7Config(self):
        url = "%sconfig/getUserVip7Config" % (config.API_ADDRESS);
        inputParam = InGetUserVip7Config(config.API_KEY, config.USER_ID);
        data = ConvertObj.convert_to_dict(inputParam);
        print(config.USER_ID)
        interface_result = HttpRequest.requestInterface(url, data)
        assert interface_result.result_status == config.INTERFACE_SUCCESS_STATUS, "接口返回码错误";
        object = interface_result.error_reason;
        print(object["code"]);
        if object['code'] == 10004:
            print(object["version"]);
            assert object['version'] is not None, "版本号不能为空"
            print(object["msg"]);
        assert object['msg'] is not None, "错误信息不能为空"

        if object['code'] == config.INTERFACE_SUCCESS_CODE:
            data_info = object["data"];
            print(data_info['confValue']);
            assert data_info['confValue'] is not None, "开关value不能为空"
            print(data_info['confKey']);
            assert data_info['confKey'] is not None, "开关key不能为空"
            print(data_info['description']);
            assert data_info['description'] is not None, "开通vip图片地址不存在"
            vip_pic = get_url_isexist(data_info['description'])
            assert vip_pic == config.URL_SUCCESS_CODE, "开通vip图片地址访问不到";

    # 根据身份获取首页的热门推荐
    def getNewHomeRecommend_qr(self, parent_identity_id, identity_id):
        url = "%sgetNewHomeRecommend" % (config.API_ADDRESS);
        inputParam = INGetNewHomeRecommend(config.API_KEY, parent_identity_id, identity_id);
        data = ConvertObj.convert_to_dict(inputParam);
        interface_result = HttpRequest.requestInterface(url, data)
        assert interface_result.result_status == config.INTERFACE_SUCCESS_STATUS, "接口返回码错误";
        object = interface_result.error_reason;
        assert object["code"] == config.INTERFACE_SUCCESS_CODE, "获取信息失败";
        data_info = object["data"];
        print(data_info)
        # 二维码列表
        obj = data_info['qrCode'];
        print(obj['total_count']);
        for qr in obj['data']:
            print("begin-----get----------二维码列表-----------------------------------")
            print(qr['id']);
            print(qr['title']);
            print(qr['content']);
            print(qr['img_url']);
            print(qr['sort']);
            assert qr['id'] is not None, "id不能为空"
            assert qr['title'] is not None, "标题不能为空"
            assert qr['content'] is not None, "内容不能为空"
            assert qr['img_url'] is not None, "图片地址不能为空"
            assert qr['sort'] is not None, "sort不能为空"
            img_url = get_url_isexist(qr['img_url'])
            assert img_url == config.URL_SUCCESS_CODE, "二维码地址访问不到";

    def getNewHomeRecommend_video(self, parent_identity_id, identity_id):
        url = "%sgetNewHomeRecommend" % (config.API_ADDRESS);
        inputParam = INGetNewHomeRecommend(config.API_KEY, parent_identity_id, identity_id);
        data = ConvertObj.convert_to_dict(inputParam);
        interface_result = HttpRequest.requestInterface(url, data)
        assert interface_result.result_status == config.INTERFACE_SUCCESS_STATUS, "接口返回码错误";
        object = interface_result.error_reason;
        assert object["code"] == config.INTERFACE_SUCCESS_CODE, "获取信息失败";
        data_info = object["data"];
        print(data_info);

        video = data_info['video'];
        total_count = video['total_count'];
        print(total_count);
        curl_count = len(video['data']);
        assert total_count == curl_count, "实际得到的数量与total_count不一致"
        for obj_video in video['data']:
            print(obj_video['title']);
            print(obj_video['hd_url']);
            print(obj_video['sd_url']);
            print(obj_video['fhd_url']);
            print(obj_video['img_url']);
            print(obj_video['courseware_id']);

            assert obj_video['title'] is not None, "title不能为空"
            assert obj_video['hd_url'] is not None, "fhd_url地址不能为空"
            assert obj_video['sd_url'] is not None, "fhd_url地址不能为空"
            assert obj_video['fhd_url'] is not None, "fhd_url地址不能为空"
            assert obj_video['img_url'] is not None, "图片地址不能为空"
            assert obj_video['courseware_id'] is not None, "课件ID不能为空"
            img_url = get_url_isexist(obj_video['img_url'])
            assert img_url == config.URL_SUCCESS_CODE, "图片地址访问不到";

            # 校验推荐的课程

    def getNewHomeRecommend_carouselfigure(self, parent_identity_id, identity_id):
        url = "%sgetNewHomeRecommend" % (config.API_ADDRESS);
        inputParam = INGetNewHomeRecommend(config.API_KEY, parent_identity_id, identity_id);
        data = ConvertObj.convert_to_dict(inputParam);
        interface_result = HttpRequest.requestInterface(url, data)
        assert interface_result.result_status == config.INTERFACE_SUCCESS_STATUS, "接口返回码错误";
        object = interface_result.error_reason;
        assert object["code"] == config.INTERFACE_SUCCESS_CODE, "获取信息失败";
        data_info = object["data"];
        print(data_info);
        obj = data_info['carouselfigure'];
        print(obj['total_count']);
        for obj_detail in obj['data']:
            print(obj_detail['id']);
            print(obj_detail['content']);
            print(obj_detail['content_type']);
            print(obj_detail['title']);
            print(obj_detail['img_url']);
            print(obj_detail['sort']);

            assert obj_detail['id'] is not None, "id不能为空"
            assert obj_detail['content'] is not None, "内容不能为空"
            assert obj_detail['content_type'] is not None, "内容类型不能为空"
            assert obj_detail['title'] is not None, "标题不能为空"
            assert obj_detail['img_url'] is not None, "图片地址不能为空"
            assert obj_detail['sort'] is not None, "sort不能为空"
            img_url = get_url_isexist(obj_detail['img_url'])
            assert img_url == config.URL_SUCCESS_CODE, "课程地址地址访问不到";



            # 日志记录 自动播放

    def test_playSettings(self):
        url = "%splaySettings" % (config.API_ADDRESS);
        inputParam = InPlaySettings(config.API_KEY);
        data = ConvertObj.convert_to_dict(inputParam);
        interface_result = HttpRequest.requestInterface(url, data)
        assert interface_result.result_status == config.INTERFACE_SUCCESS_STATUS, "接口返回码错误";
        object = interface_result.error_reason;
        print(object["code"]);
        if object['code'] == 10004:
            print(object["version"]);
            assert object['version'] is not None, "版本号不能为空"
            print(object["msg"]);
            assert object['msg'] is not None, "错误信息不能为空"

        if object['code'] == config.INTERFACE_SUCCESS_CODE:
            assert object['code'] is not None, "提示语句"


            # 清除用户历史记录

    def test_clearWatchHistory(self):
        url = "%sclearWatchHistory" % (config.API_ADDRESS);
        inputParam = InClearWatchHistory(config.API_KEY, config.USER_ID);
        data = ConvertObj.convert_to_dict(inputParam);
        interface_result = HttpRequest.requestInterface(url, data)
        assert interface_result.result_status == config.INTERFACE_SUCCESS_STATUS, "接口返回码错误";
        object = interface_result.error_reason;
        code = object['code'];
        print(code);
        assert code == config.INTERFACE_SUCCESS_CODE, "清除用户历史记录失败"



        # 获取vip分类下的推荐课程

    def test_getCategoryCourseList(self):
        url = "%sgetCategoryCourseList/%s" % (config.API_ADDRESS, COURSE_TYPE);
        inputParam = InGetCategoryCourseList(config.API_KEY, PAGE_NUMBER, PAGE_SIZE, COURSE_TYPE);
        data = ConvertObj.convert_to_dict(inputParam);
        interface_result = HttpRequest.requestInterface(url, data)
        assert interface_result.result_status == config.INTERFACE_SUCCESS_STATUS, "接口返回码错误";
        object = interface_result.error_reason;
        print(object)
        code = object['code'];
        print(code);
        assert code == config.INTERFACE_SUCCESS_CODE, "清除用户历史记录失败";

        object = interface_result.error_reason;
        for object_info in object['data']:
            print(object_info['id']);
            assert object_info['id'] is not None, "版本号不能为空"
            print(object_info['name']);
            assert object_info['name'] is not None, "课程名称不能为空"
            print(object_info['name_us']);
            assert object_info['name_us'] is not None, "课程英文名称不能为空"
            print(object_info['img_url']);
            assert object_info['img_url'] is not None, "课程图片不能为空"
            print(object_info['courseware_total_count']);
            assert object_info['courseware_total_count'] is not None, "课件总数不能为空"
            print(object_info['type']);
            assert object_info['type'] is not None, "类型不能为空"
            print(object_info['watch_count']);
            assert object_info['watch_count'] is not None, "观看数量不能为空"

            print("--------------------------------------------------")



    # 获取9大分类
    def get_vip_course_categories(self):
        url = "%sgetVipCourseCategories" % (config.API_ADDRESS);
        inputParam = InGetVipCourseCategories(config.API_KEY, PAGE_NUMBER, PAGE_SIZE);
        data = ConvertObj.convert_to_dict(inputParam);
        interface_result = HttpRequest.requestInterface(url, data)
        assert interface_result.result_status == config.INTERFACE_SUCCESS_STATUS, "接口返回码错误";
        object = interface_result.error_reason;
        for object_info in object['data']:
            print(object_info['id']);
            assert object_info['id'] is not None, "id不能为空";
            print(object_info['name']);
            assert object_info['name'] is not None, "名字不能为空"
            print(object_info['sort']);
            assert object_info['sort'] is not None, "排序不能为空"
            print(object_info['img_url']);
            assert object_info['img_url'] is not None, "图片地址不能为空"

            print(object_info['img_url_v3']);
            assert object_info['img_url_v3'] is not None, "3.0分类图片地址不能为空"
            print(object_info['status']);
            assert object_info['status'] is not None, "状态不能为空"

            img_url = get_url_isexist(object_info['img_url'])
            assert img_url == config.URL_SUCCESS_CODE, "分类图片地址不能为空";

            img_url_v3 = get_url_isexist(object_info['img_url_v3'])
            assert img_url_v3 == config.URL_SUCCESS_CODE, "3.0分类图片地址不能为空";
            print("--------------------------------------------------")
        return object;


    # 获取个性推荐课程
    def test_getRecommendList(self):
        identity_ID = 7;
        PARENT_IDENTITY_ID = 1;
        url = "%sgetRecommendList/%s" % (config.API_ADDRESS, CONTENT_ID);
        inputParam = InGetRecommendList(config.API_KEY, PAGE_NUMBER, PAGE_SIZE, TYPE, PARENT_IDENTITY_ID, identity_ID,
                                        CONTENT_ID);
        data = ConvertObj.convert_to_dict(inputParam);
        interface_result = HttpRequest.requestInterface(url, data)
        assert interface_result.result_status == config.INTERFACE_SUCCESS_STATUS, "接口返回码错误";
        object = interface_result.error_reason;
        for object_info in object['data']:
            print(object_info['id']);
            assert object_info['id'] is not None, "id不能为空";
            print(object_info['name']);
            assert object_info['name'] is not None, "课程图片不能为空";
            print(object_info['name_us']);
            assert object_info['name_us'] is not None, "课程英文名称不能为空";
            print(object_info['img_url']);
            assert object_info['img_url'] is not None, "图片地址不能为空";
            print(object_info['courseware_total_count']);
            assert object_info['courseware_total_count'] is not None, "课件总数不能为空";
            print("--------------------------------------------------")


            # 清除用户收藏行为

    def test_update_user_identity(self, sub_identity):
        url = "%sidentity/updateUserIdentity/%s" % (config.API_ADDRESS, sub_identity);
        inputParam = InUpdateUserIdentity(config.API_KEY, config.USER_ID, CHANNEL,SELECT_TYPE);
        data = ConvertObj.convert_to_dict(inputParam);
        interface_result = HttpRequest.requestInterface(url, data)
        assert interface_result.result_status == config.INTERFACE_SUCCESS_STATUS, "接口返回码错误";
        object = interface_result.error_reason;
        code = object['code'];
        print(code);
        assert code == config.INTERFACE_SUCCESS_CODE, "设置用户身份失败"

# def tearDown(self):
#     print("end.........")
