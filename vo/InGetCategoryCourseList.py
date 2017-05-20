class InGetCategoryCourseList:
    apikey = '';
    page_number = '';
    page_size = '';
    type = '';

    def __init__(self, api_key, page_number, page_size, type):
        self.apikey = api_key;
        self.page_number = page_number;
        self.page_size = page_size;
        self.type = type;
