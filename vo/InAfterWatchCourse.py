class InAfterWatchCourse:
    apikey = '';
    uid = '';
    course_id = '';
    courseware_id = '';
    time_point = 0;
    status = 0;
    studystatus = 0;
    is_vip = 0;
    registerid = '';


    def __init__(self, api_key, uid, course_id, course_ware_id, time_point, status, study_status, is_vip, register_id):
        self.apikey = api_key;
        self.uid = uid;
        self.course_id = course_id;
        self.courseware_id = course_ware_id;
        self.time_point = time_point;
        self.status = status;
        self.studystatus = study_status;
        self.is_vip = is_vip;
        self.registerid = register_id;



