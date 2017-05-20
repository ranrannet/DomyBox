class InGetCourseList:
    apikey = '';
    subject_id="";
    cid=0;
    sort=0;
    condition ="";


    def __init__(self, apikey, cid, subject_id, sort):
        self.apikey = apikey;
        self.cid =cid;
        self.subject_id = subject_id;
        self.sort = sort;
        # self.condition = condition;
        # "16:68"



