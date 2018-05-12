# coding=utf-8
from tornado.web import url
import controller.handlers
handlers = [
    url(r'/',controller.handlers.IndexHandler, name='index'),
]
