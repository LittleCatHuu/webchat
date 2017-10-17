#coding=utf-8
import hashlib
import web
import lxml
import time
import os

class WeichatInterface:
    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates__root = os.path.join(self.app_root,'templates')
        self.render = web.template.render(self.templates__root)

    def GET(self):
        #获取输入参数
        data = web.input()
        signature = data.signature
        timestamp = data.timestamp
        nonce = data.nonce
        echostr = data.echostr
        #公众号的token
        token = "weixin"
        #list排序
        list = [token,timestamp,nonce]
        list.sort()
        sha1 = hashlib.sha1()
        map(sha1.update,list)
        hashcode = sha1.hexdigest() 

        #如果是来自微信的请求，则回复echostr
        if  hashcode == signature:
            return echostr