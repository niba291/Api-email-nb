#!/usr/bin/env python
# -*- coding: utf-8 -*-
# IMPORT=====================================================================================================================
from multiprocessing import context
from eventException import eventException 
from email.message  import EmailMessage
import ssl
import smtplib
# CLASS======================================================================================================================
class classEmail:
# VAIRABLES==================================================================================================================
    emailfrom               = ""
    password                = ""    
    to                      = None
    subjet                  = None
    body                    = None
    objEmail                = None
    objcontext              = None
    statusError             = None
# INIT=======================================================================================================================
    def __init__(self): 
        try:
            self.objEmail   = EmailMessage()
        except Exception as ex:
            eventException(ex)

    def send(self, json):
        try:
            if "to" in json:
                self.to             = json["to"]
            else:
                return {'status': 1, 'message-en': 'Not existing \'to\'', 'message-es': 'No existente \'to\''}

            if "subject" in json:
                self.subjet         = json["subject"]
            else:
                return {'status': 1, 'message-en': 'Not existing \'subject\'', 'message-es': 'No existente \'subject\''}

            if "body" in json:
                self.body           = json["body"]
            else:
                return {'status': 1, 'message-en': 'Not existing \'body\'', 'message-es': 'No existente \'body\''}

            self.objEmail["From"]       = self.emailfrom
            self.objEmail["To"]         = self.to
            self.objEmail["subject"]    = self.subjet
            self.objEmail.set_content(self.body)
            self.context                = ssl.create_default_context()

            smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465, context = self.objcontext) 
            smtp.login(self.emailfrom, self.password)
            smtp.sendmail(self.emailfrom, self.to, self.objEmail.as_string())

            return {'status': 0, 'message-en': 'Email sent', 'message-es': 'Email enviado'}
        except Exception as ex:
            eventException(ex)
            return ({'status': 1, 'message-en': 'Exection', 'message-es': 'Exection'})
# CLOSE CLASS================================================================================================================
