#!/usr/bin/env python
# -*- coding: utf-8 -*-
# IMPORT=====================================================================================================================
import sys
import os
# CLASS======================================================================================================================
class eventException:
# VAIRABLES==================================================================================================================
    exc_type                = None    
    exc_obj                 = None
    exc_tb                  = None
    fname                   = None
    strSheet                = None
    strMessage              = None
    nameApp                 = "Api-email-nb"    
# INIT=======================================================================================================================
    def __init__(self, ex): 
        self.exc_type, self.exc_obj, self.exc_tb = sys.exc_info()
        self.fname          = os.path.split(self.exc_tb.tb_frame.f_code.co_filename)[1]    
        self.strSheet       = str(self.fname)
        self.strMessage     = "PYTHON: " + self.strSheet + " \"" + self.nameApp + "\"", type(ex).__name__, str(ex),(self.strSheet + " " + str(self.exc_tb.tb_lineno))
        print(self.strMessage)
        return self.strMessage
# CLOSE CLASS================================================================================================================