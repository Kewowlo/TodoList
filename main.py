#!/usr/bin/env python

import os

import tornado.autoreload
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options

import controller.handlers
import pymongo
from config import CONFIG
from url_mapping import handlers
import log_manager
settings = {
    "static_path" : os.path.join(os.path.dirname(__file__), "static"),
    "template_path" : os.path.join(os.path.dirname(__file__), "templates"),
    "login_url" : CONFIG["login_url"],
    'debug' : CONFIG["debug"],
}

define("port", default=8888, help="run on the given port", type=int)
class Application(tornado.web.Application):
    def __init__(self):
        conn = pymongo.MongoClient('localhost',27017)
        self.db = conn['todolist']
        super(Application, self).__init__(handlers, **settings)


if __name__ == '__main__':
    tornado.options.parse_command_line()
    log_manager.init(CONFIG['port'], CONFIG['log_console'], CONFIG['log_file'], None, CONFIG['log_level'])
    app = Application()
    CONFIG['application'] = app 
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
