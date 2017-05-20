class InGetCoursewareInfo:
    apikey = '';
    uid = '';
    course_id = '';
    courseware_id = '';
    time_point = 0;
    status = 0;
    studystatus = 0;
    is_vip = 0;
    platform_type = 1;


    def __init__(self, api_key, uid, course_id, course_ware_id, time_point, status, study_status, is_vip, platform_type):
        self.apikey = api_key;
        self.uid = uid;
        self.course_id = course_id;
        self.courseware_id = course_ware_id;
        self.time_point = time_point;
        self.status = status;
        self.studystatus = study_status;
        self.is_vip = is_vip;
        self.platform_type = platform_type;



