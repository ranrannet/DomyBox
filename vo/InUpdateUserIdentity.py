class InUpdateUserIdentity:
    uid = "";
    channel = "";
    select_type = "";
    apikey = "";

    def __init__(self, api_key, user_id, select_type, channel):
        self.uid = user_id;
        self.channel = channel;
        self.select_type = select_type;
        self.apikey = api_key;
