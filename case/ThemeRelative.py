# coding: utf-8

# import urllib2

from util import ConvertObj
from util import HttpRequest
from util import config
from urllib import request

from util.UtilMethod import get_url_isexist
from vo.InGetFavorTheme import InGetFavorTheme
from vo.InGetFavorThemeList import InGetFavorThemeList

from vo.InGetThemeInfo import InGetThemeInfo
from vo.InGetThemeList import InGetThemeList
from vo.InGetRelativeTheme import InGetRelativeTheme
from vo.InFavorTheme import InFavorTheme;
from vo.ResultObject import ResultObject


def getFavorThemeList():
    url = "%sgetFavorThemeList" % config.API_ADDRESS;
    favorTheme = InGetFavorThemeList(config.API_KEY, config.USER_ID, 0, 36, 'DMA31105150914191');
    data = ConvertObj.convert_to_dict(favorTheme);
    interface_result = HttpRequest.requestInterface(url, data);
    assert interface_result.result_status == config.INTERFACE_SUCCESS_STATUS, "接口返回码错误";
    object = interface_result.error_reason;
    for object_info in object['data']:
        assert object_info['id'] is not None, "id不能为空";
        assert object_info['img_url'] is not None, "图片Url不能为空";
        assert object_info['name'] is not None, "专题图片不能为空";
        url = object_info['img_url'];
        img_url_http_code = get_url_isexist(url)
        assert img_url_http_code == config.URL_SUCCESS_CODE, "图片地址不存在";


def getThemeInfo():
    url = "%sgetThemeInfo" % config.API_ADDRESS;
    themeInfo = InGetThemeInfo(config.API_KEY, config.USER_ID, 'TH314');
    data = ConvertObj.convert_to_dict(themeInfo);
    interface_result = HttpRequest.requestInterface(url, data)
    assert interface_result.result_status == config.INTERFACE_SUCCESS_STATUS, "接口返回码错误";
    object = interface_result.error_reason;
    for object_info in object['data']:
        assert object_info['name'] is not None, "专题名称不能为空";
        assert object_info['background_img_url'] is not None, "背景图片不能为空";
        assert object_info['img_url'] is not None, "缩略图片不能为空";
        background_http_code = get_url_isexist(object_info['background_img_url'])
        assert background_http_code == config.URL_SUCCESS_CODE, "背景图片地址不存在";
        background_http_code = get_url_isexist(object_info['img_url'])
        assert background_http_code == config.URL_SUCCESS_CODE, "缩略图片地址不存在";




def getThemeList():
    url = "%sgetThemeList" % config.API_ADDRESS;
    themeInfo = InGetThemeList(config.API_KEY, 0, 20);
    data = ConvertObj.convert_to_dict(themeInfo);
    interface_result = HttpRequest.requestInterface(url, data)
    assert interface_result.result_status == config.INTERFACE_SUCCESS_STATUS, "接口返回码错误"
    object = interface_result.error_reason;
    for theme in object['data']:
        assert theme['id'] is not None, "id 不能为空";
        assert theme['img_url'] is not None, "img_url 不能为空";
        assert theme['name'] is not None, "专题名称 不能为空";
        img_url_http_code = get_url_isexist(theme['img_url'])
        assert img_url_http_code == config.URL_SUCCESS_CODE, "缩略图片地址不存在";



def getRelativeTheme():
    url = "%sgetRelativeTheme" % config.API_ADDRESS;
    print(url);
    relativeTheme = InGetRelativeTheme(config.API_KEY, 'TH107');
    data = ConvertObj.convert_to_dict(relativeTheme);
    interface_result = HttpRequest.requestInterface(url, data)
    assert interface_result.result_status == config.INTERFACE_SUCCESS_STATUS, "接口返回码错误"
    object = interface_result.error_reason;
    assert object['code'] == config.INTERFACE_SUCCESS_CODE, "获取相关专题失败";


# 收藏专题
def favorTheme():
    url = "%sfavorTheme" % config.API_ADDRESS;
    print(url);
    relativeTheme = InFavorTheme(config.API_KEY, config.USER_ID, 'TH107');
    data = ConvertObj.convert_to_dict(relativeTheme);
    interface_result = HttpRequest.requestInterface(url, data)
    assert interface_result.result_status == config.INTERFACE_SUCCESS_STATUS, "接口返回码错误";
    object = interface_result.error_reason;
    assert object['code'] == config.INTERFACE_SUCCESS_CODE, "收藏专题失败";
