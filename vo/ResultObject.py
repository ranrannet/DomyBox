class ResultObject:
    result_status = "";
    error_list = "";
    right_list = "";
    method_name_english = "";
    method_name_china = "";
    object_info = "";

    def __init__(self, method_name_english, method_name_china,result_status, error_list, right_list, object_info):
        self.method_name_english = method_name_english;
        self.method_name_china = method_name_china;
        self.result_status = result_status;
        self.error_list = error_list;
        self.right_list = right_list;
        self.object_info = object_info;
