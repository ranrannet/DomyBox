# coding: utf-8

import json;

from util import ConvertObj
from util import HttpRequest
from util import config
from urllib import request, parse

from vo.InGetHomeRecommend import InGetHomeRecommend;

# 项目类型  1为鹏云课堂盒子 2、网站
PROJECT_TYPE = 1


def getHomeRecommend():
    url = "%sgetHomeRecommend" % config.API_ADDRESS;
    favorTheme = InGetHomeRecommend(config.API_KEY, PROJECT_TYPE, config.USER_ID);  # 将对象转成字典
    data = ConvertObj.convert_to_dict(favorTheme);
    interface_result = HttpRequest.requestInterface(url, data);

    assert interface_result.result_status == config.INTERFACE_SUCCESS_STATUS, "接口返回码错误"
    object = interface_result.error_reason;
    assert object['code'] == config.INTERFACE_SUCCESS_CODE, "获取相关专题失败";
    for favorTheme in object['data']:
        check_banner_url_is_exist(favorTheme)  # 判断banner地址是否存在


def check_banner_url_is_exist(favorTheme):
    img_url_tv = favorTheme['img_url_tv'];
    s = json.loads(img_url_tv);
    img_url_tv = s["740_440"];
    f = request.urlopen(img_url_tv)
    print(f.code)
    if (f.code == config.URL_SUCCESS_CODE):
        assert f.code == config.URL_SUCCESS_CODE, "banner地址不正常";
