class InterfaceResultObject:
    result_status = "";
    error_reason = "";
    error_value= "";
    test_method= ""


    def __init__(self, result_status, error_reason):
        self.result_status = result_status;
        self.error_reason = error_reason;

