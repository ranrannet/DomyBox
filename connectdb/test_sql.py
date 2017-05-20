# -*- coding: utf-8 -*-
import unittest

import pymysql

from util import ConvertObj
from connectdb import IndentityVo;


class test_sql(unittest.TestCase):
    def setUp(self):
        print("in......")


    def test_get_sub_identity(self,parent_id,i):
        l1 = ['id', 'name', 'sort']
        global conn, cur
        conn = pymysql.connect(host='118.144.248.23', port=3307, user='mmysql', passwd='m12345', db='pengCloud',
                               charset='utf8')
        cur = conn.cursor()
        cur.execute("SELECT id,name,sort FROM identity  where parent_id =%s and status =1" % parent_id);
        lists = list(cur.fetchall());
        l2 = list(lists[i]);
        dicts = zip(l1, l2);
        obj = dict(dicts);
        print(obj['id'])
        return obj;


def tearDown(self):
    print("end.........")
