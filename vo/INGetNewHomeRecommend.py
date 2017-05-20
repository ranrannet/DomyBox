class INGetNewHomeRecommend:
    apikey = "";
    identityId = "";
    parentIdentityId = "";

    def __init__(self, api_key, parent_identity_id,identity_id):
        self.apikey = api_key;
        self.identityId = identity_id;
        self.parentIdentityId = parent_identity_id;
