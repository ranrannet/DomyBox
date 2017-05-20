class InGetRecommendList:
    apikey = '';
    page_number = '';
    page_size = '';
    type = "";
    parentIdentityId = '';
    identityId = '';
    content = "";

    def __init__(self, api_key, page_number, page_size, type, parent_indentity_id, indentity_id, content_id):
        self.apikey = api_key;
        self.page_number = page_number;
        self.page_size = page_size;
        self.type =type;
        self.parentIdentityId = parent_indentity_id;
        self.identityId = indentity_id;
        self.content = content_id;