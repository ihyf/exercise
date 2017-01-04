# coding:utf-8
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import os

from tornado.options import define, options

define("port", default=8888, help="run on the givern port", type=int)

'''
1.import 语句
2.选项参数定义
3.Application定义
4.BaseHandler定义
5.XXHandlers定义
6.main()定义
'''


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.write("hellow hyf")


def main():
    tornado.options.parse_command_line()
    application = tornado.web.Application([  # 获得application实例
        (r"/hello.htm", MainHandler),
    ],
        debug=True,
        template_path=os.path.join(os.path.dirname(__file__), 'templates'),
        static=os.path.join(os.path.dirname(__file__), 'static'),
    )
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
if __name__ == '__main__':
    main()