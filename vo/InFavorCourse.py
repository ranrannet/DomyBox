class InFavorCourse:
    apikey = '';
    uid = '';
    course_id = 0;


    def __init__(self,course_id, uid, api_key):
        self.apikey = api_key;
        self.uid = uid;
        self.course_id = course_id;
