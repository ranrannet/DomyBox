# coding: utf-8
from util import HttpRequest
from util import config

from util import ConvertObj
from vo.InSendEmailMessage import InSendEmailMessage


def sendEmailMessage(title, content):
    sendEmailParam = InSendEmailMessage(config.RECEIVE_EMAIL, config.SEND_EMAIL, title, content);
    data = ConvertObj.convert_to_dict(sendEmailParam);
    interface_result = HttpRequest.requestInterfaceSame(config.EMAIL_ADDRESS, data);
    print(interface_result);

    print(interface_result.result_status);
    return interface_result.result_status;
