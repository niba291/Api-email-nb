#!/usr/bin/env python
# -*- coding: utf-8 -*-
# IMPORT=====================================================================================================================
from flask          import Flask, jsonify, request
from classEmail     import classEmail
from eventException import eventException 
# VARIABLES==================================================================================================================
app                     = Flask(__name__)
# ROUTE======================================================================================================================
@app.route("/EmailSend", methods = ["POST"])
def EmailSend():
    try:
        json            = request.get_json(force=True)
        objEmail        = classEmail()        
        return jsonify(objEmail.send(json))
    except Exception as ex:        
        objEmail        = classEmail()        
        objEmail.send({
            "to"        : "lectoresdelmanga.errors@gmail.com",
            "subject"   : "Error rank 1",
            "body"      : eventException(ex)
        })
        return jsonify({'status': 1, 'message-en': 'Exection', 'message-es': 'Exection'})

# CONFIG=====================================================================================================================
if __name__ == "__main__":
    app.run(debug=True, port=5000)

