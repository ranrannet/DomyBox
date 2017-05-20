# coding: utf-8
from urllib import request


def get_url_isexist(pic_url):
    response = request.urlopen(pic_url, timeout=3)
    httpCode = response.getcode()
    return httpCode
