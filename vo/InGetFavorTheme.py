class InGetFavorTheme:
    apikey = '';
    uid = '';
    page_number = 0;
    page_size = 0;
    registerid = '';

    def __init__(self, api_key, uid, pageNumber, pageSize, registerId):
        self.apikey = api_key;
        self.uid = uid;
        self.page_number = pageNumber;
        self.page_size = pageSize;
        self.registerid = registerId;
