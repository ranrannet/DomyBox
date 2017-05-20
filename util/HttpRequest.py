# coding: utf-8
import json
# import urllib2, urllib
from urllib import request, parse

import time

from util import config
from vo.InterfaceResultObject import InterfaceResultObject;


# 从数据库中获取一条数据
def requestInterface(_url, _data):
    try:
        data = parse.urlencode(_data).encode('utf-8')
        url2 = request.Request(_url, data)  # 用.Request来发送POST请求，指明请求目标是之前定义过的url，请求内容放在data里
        response = request.urlopen(url2)  # 用.urlopen打开上一步返回的结果，得到请求后的响应内容
        data_json = response.read().decode('utf-8');
        assert request.urlopen(url2).code == config.URL_SUCCESS_CODE,"接口请求错误";
        jsonData = json.loads(data_json)

        return InterfaceResultObject("success", jsonData);
    except request.HTTPError as e:
        return InterfaceResultObject("error", e);
    except request.URLError as e:
        return InterfaceResultObject("error", str(e));


# 从数据库中获取一条数据
def requestInterfaceSame(_url, _data):
    try:
        data = parse.urlencode(_data).encode('utf-8')  # 把参数进行编码
        url2 = urllib2.Request(_url, data)  # 用.Request来发送POST请求，指明请求目标是之前定义过的url，请求内容放在data里
        response = urllib2.urlopen(url2)  # 用.urlopen打开上一步返回的结果，得到请求后的响应内容
        apicontent = response.read()  # 将响应内容用read()读取出来
        return InterfaceResultObject("success", apicontent);
    except urllib2.HTTPError as e:
        print
        return InterfaceResultObject("error", e.code);
    except urllib2.URLError as e:
        print(str(e))
        return InterfaceResultObject("error", str(e));


# 读取html文件
def read_html(html_template):
    file_object = open(html_template)
    try:
        html_template = file_object.read()
    finally:
        file_object.close()

    return html_template;
