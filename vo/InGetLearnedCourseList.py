class InGetLearnedCourseList:
    apikey="";
    theme_id = '';
    uid=0;
    type=0;
    page_number=0;
    page_size=0;


    def __init__(self,apikey, theme_id,uid,type, page_number, page_size):
        self.apikey =apikey;
        self.theme_id = theme_id;
        self.uid = uid;
        self.type = type;
        self.page_number = page_number;
        self.page_size = page_size;


