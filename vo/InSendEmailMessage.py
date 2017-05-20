class InSendEmailMessage:

    to = '';
    cc = '';
    subject = '';
    content = '';

    def __init__(self, to, cc, subject, content):
        self.to = to;
        self.cc = cc;
        self.subject = subject;
        self.content = content;
