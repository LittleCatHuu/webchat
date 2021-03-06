#   coding=utf-8
import os
import sae
import web
from webchatinterface import webchatinterface

urls = ('weixin','WebchatInterface')

app_root = os.path.dirname(__file__)
templates_root = os.path.join(app_root,'templates')
render = web.tmplate.render(templates_root)

app = web.application(urls,globals()).wsgifunc()
application = sae.create_wsgi_app(app)