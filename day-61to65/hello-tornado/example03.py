import os
import re
import tornado.ioloop
import tornado.web
from tornado.options import define, options, parse_command_line

define('port', default=8000, type=int)

user = {}

class User(object):
    def __init__(self, nickname, gender, birthday):
        self.nickname = nickname
        self.gender = gender
        self.birthday = birthday

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        nickname = self.get_cookie('nickname')
        if nickname in user:
            self.render('userinfo.html', user=user[nickname])
        else:
            self.render('userform.html', hint='请填写个人信息')

class UserHandler(tornado.web.RequestHandler):
    def post(self):
        nickname = self.get_body_argument('nickname').strip()
        gender = self.get_body_argument('gender')
        birthday = self.get_body_argument('birthday')
        if not re.fullmatch(r'\w{6,20}', nickname):
            self.render('userform.html', hint='请输入有效的昵称')
        elif nickname in user:
            self.render('userform.html', hint='昵称已经被占用')
        else:
            user[nickname] = User(nickname, gender, birthday)
            self.set_cookie('nickname', nickname, expires_days=7)
            self.render('userinfo.html', user=user[nickname])

def post_handler_test():
    parse_command_line()
    app = tornado.web.Application(
        handlers=[
            (r'/', MainHandler),
            (r'/register', UserHandler),
        ], template_path = os.path.join(os.path.dirname(__file__), 'templates')
    )
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    post_handler_test()