class InGetCoursewareList:
    apikey = '';
    uid = 0;
    course_id = '';
    type = 0;
    page_number = 0;
    page_size = 0;


    def __init__(self, api_key,course_id, uid,type , page_size, page_number):
        self.apikey = api_key;
        self.uid = uid;
        self.course_id = course_id;
        self.type = type;
        self.page_size = page_size;
        self.page_number = page_number;
