# coding: utf-8

# from TestCase.CourseRelative import CourseRelative
# import CourseWareRelative;
# import ThemeRelative;
# import UserAction;


# 专题相关接口-----------------------------------------------------
# 收藏专题
from case import ThemeRelative

favor_theme = ThemeRelative.favorTheme();
# 获取收藏专题列表
ThemeRelative.getFavorThemeList();
# 获取相关专题
ThemeRelative.getRelativeTheme();
# 获取专题详情
ThemeRelative.getThemeInfo();
# 获取专题列表
ThemeRelative.getThemeList();



# 用户行为相关接口-----------------------------------------------------


# # 收藏
UserAction.favorCourse();

# 点赞
UserAction.praiseCourse();



#课件相关接口---------------------------------------------------------------

# 观看后上报观看行为
CourseWareRelative.afterWatchCourse();

# 清空观看历史
CourseWareRelative.clearWatchHistory();

# 获取课件详情
CourseWareRelative.getCoursewareInfo();


# 获取课件列表
CourseWareRelative.getCoursewareList();

# 获取观看历史
CourseWareRelative.getWatchHistory();


#课程相关接口---------------------------------------------------------------


# 获取一个分类下的科目列表
CourseRelative.getCategorySubjects();

# # 获取课程分类列表
CourseRelative.getCourseCategories();


# # 获取课程详情
CourseRelative.getCourseInfo();



# # 根据科目获取课程列表
CourseRelative.getCourseList();

CourseRelative.getFavorCourseList();
# 获取收藏的课程列表
# getFavorCourseList
# getFilterConditionList


# 获取已学完未学完的课程列表
CourseRelative.getLearnedCourseList();
#获取一个专题的课程列表
CourseRelative.getThemeCourseList();



#----------------热门推荐-----------------------------------
# 获取首页banner
HomeRecommend.getHomeRecommend();






# 未测试












#
# email_content = "";
# i = 0;
# for interface in set:
#     i = i + 1;
#     print(i);
#     error_result_list = " ";
#     right_result_list = " ";
#     result_status = interface.__dict__["result_status"];
#     method_name_english = interface.__dict__["method_name_english"];
#     method_name_china = interface.__dict__["method_name_china"];
#     object_info = interface.__dict__["object_info"];
#
#     for error_info in interface.__dict__["error_list"]:
#         if (error_info != 0):
#             error_result_list += error_info + "\n</br>";
#
#     for right_info in interface.__dict__["right_list"]:
#         if (right_info != 0):
#             right_result_list += right_info + "\n</br>";
#     html_content = "";
#
#     tr_content = config.TR_CONTENT;
#     emailContent = tr_content.format(
#         i, method_name_english, method_name_china, result_status, error_result_list, right_result_list, i, i,
#         object_info);
#     email_content += emailContent;
#
# html_template = HttpRequest.read_html("html_template.html");
#
# email_html_content = html_template.replace("{content}", email_content);
#
# print(email_html_content);
#
# sendResult = SendEmail.sendEmailMessage("电视盒子接口测试", email_html_content);
# print(sendResult);
