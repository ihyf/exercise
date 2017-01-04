# coding:utf-8
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.tcelery
from tornado.web import asynchronous
from tasks import query_users
from tornado.options import define, options

tornado.tcelery.setup_nonblocking_producer()

define("port", default=8888, help="run on the givern port", type=int)

'''
1.import 语句
2.选项参数定义
3.Application定义
4.BaseHandler定义
5.XXHandlers定义
6.main()定义
'''


class MainHandler(tornado.web.RequestHandler):  # 普通

    def get(self):
        self.write("hellow hyf")


class Asynchronous(tornado.web.RequestHandler):

    @asynchronous
    def get_all_users(self, *args):  # 异步
        query_users.apply_async(args, callback=self.on_success)

    def on_success(self):
        users = 111
        self.write(users)
        self.finish()


def main():
    tornado.options.parse_command_line()
    application = tornado.web.Application([  # 获得application实例
        (r"/hello.htm", MainHandler),
    ])
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
if __name__ == '__main__':
    main()
