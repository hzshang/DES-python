#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 hzshang <hzshang15@gmail.com>
#
# Distributed under terms of the MIT license.
from flask import Flask,request,send_file
from des import encrypt_des,decrypt_des
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
app = Flask(__name__)
app.config['base'] = dir_path+"/src/"
LISTEN="0.0.0.0"
PORT=9989

@app.route('/',methods=['GET'])
def index():
    return send_file(app.config['base']+'index.html')

@app.route('/',methods=['POST'])
def post():
    data = request.form.get('input',None)
    key =request.form.get('key',None)
    type = request.form.get('type',None)
    iv = request.form.get('iv',None)
    if data is None or key is None or type is None or iv is None:
        return "Error",400
    key = key.ljust(8,'\x00')[:8]
    iv = iv.ljust(8,'\x00')[:8]
    if type == "crypto":
        ret = encrypt_des(data,key,times=8,iv=iv)
        ret = ret.encode("hex")
    else:
        data=data.decode("hex")
        ret = decrypt_des(data,key,times=8,iv=iv)
    return ret,200

def main():
    app.run(host = LISTEN,port = PORT,debug=False)
if __name__ == "__main__":
    main()
