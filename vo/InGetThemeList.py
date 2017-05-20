class InGetThemeList:
    apikey = '';
    uid = '';
    page_number = 0;
    page_size = 0;
    registerid = '';

    def __init__(self, api_key, pageNumber, pageSize):
        self.apikey = api_key;
        self.page_number = pageNumber;
        self.page_size = pageSize;