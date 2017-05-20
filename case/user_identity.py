# coding=utf-8
import os
import unittest
from case.identity import identity


class user_has_identity(unittest.TestCase):
    def setUp(self):
        print("in......")

    # 用户已选择身份流程（1）
    # def user_select_identity(self):
    #     user_identity = identity.getUserIdentity(self);
    #     data = user_identity["data"];
    #     user_identity_is_exists = data['existsIdentity'];
    #     print(user_identity_is_exists);
    #     if user_identity_is_exists == True:
    #         print("用户已经选择过身份");
    #         parent_identity_id = data["parentIdentityId"];
    #         identity_id = data["identityId"];
    #         #获取推荐的课程
    #         identity.getNewHomeRecommend_carouselfigure(self, parent_identity_id, identity_id);
    #         #获取课件
    #         identity.getNewHomeRecommend_video(self,parent_identity_id,identity_id);
    #         #二维码
    #         identity.getNewHomeRecommend_qr(self, parent_identity_id, identity_id);
    #     else:
    #         print("用户没有选择过身份");


    # 用户未选择身份流程（2）
    def test_user_no_select_identity(self):
        # 获取身份列表
        # identity.get_identity_List(self);
        # 设置身份（一级身份少儿、二级身份0-2岁）
        identity.test_update_user_identity(self,7);
        # 获取当前身份
        user_identity = identity.getUserIdentity(self);
        data = user_identity["data"];
        # 判断设置的身份与实际身份是否相符
        assert data['identityId']==7,"设置身份失败";

    def tearDown(self):
        print("end.........")
