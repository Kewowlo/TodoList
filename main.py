#!/usr/bin/env python

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.autoreload

from tornado.options import define, options
import pymongo

import os

settings = {
    'debug':True,
    "static_path" : os.path.join(os.path.dirname(__file__), "static"),
    "template_path" : os.path.join(os.path.dirname(__file__), "templates"),
    "login_url" : r"/login"
}

define("port", default=8888, help="run on the given port", type=int)
class Application(tornado.web.Application):
    def __init__(self):
        conn = pymongo.MongoClient('localhost',27017)
        self.db = conn['todolist']
        handlers = [
            (r'/', IndexHandler),
            (r'/login', LoginHandler),
            (r'/logout', LogoutHandler),
        ]
        tornado.web.Application.__init__(self, handlers, **settings)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        pass
    def post(self):
        pass
        
class LogoutHandler(tornado.web.RequestHandler):
    def get(self):
        pass


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = Application()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
