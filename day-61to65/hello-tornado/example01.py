import tornado.ioloop
import tornado.web
from tornado.options import define, options, parse_command_line

define('port', default=8000, type=int)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('<h1>Hello, Tornado</h1>')

def MainHandler_test():
    parse_command_line()
    app = tornado.web.Application(handlers=[(r'/', MainHandler),])
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    MainHandler_test()