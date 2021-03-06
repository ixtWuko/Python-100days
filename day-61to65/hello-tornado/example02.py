import os
import random
import tornado.ioloop
import tornado.web
from tornado.options import define, options, parse_command_line

define('port', default=8000, type=int)

class SayingHandler(tornado.web.RequestHandler):
    def get(self):
        sayings = [
            '世上没有绝望的处境，只有对处境绝望的人',
            '人生的道路在态度的岔口一分为二，从此通向成功或失败',
            '所谓措手不及，不是说没有时间准备，而是有时间的时候没有准备',
            '那些你认为不靠谱的人生里，充满你没有勇气做的事',
            '在自己喜欢的时间里，按照自己喜欢的方式，去做自己喜欢做的事，这便是自由',
            '有些人不属于自己，但是遇见了也弥足珍贵'
        ]
        self.render('index.html', message=random.choice(sayings))

class WeatherHandler(tornado.web.RequestHandler):
    def get(self, city):
        weathers = {
            '北京': {'temperature': '-4~4', 'pollution': '195 中度污染'},
            '成都': {'temperature': '3~9', 'pollution': '53 良'},
            '深圳': {'temperature': '20~25', 'pollution': '25 优'},
            '广州': {'temperature': '18~23', 'pollution': '56 良'},
            '上海': {'temperature': '6~8', 'pollution': '65 良'}
        }
        if city in weathers:
            self.render('weather.html', city=city, weather=weathers[city])
        else:
            self.render('index.html', message=f'没有{city}的天气信息')

class ErrorHandler(tornado.web.RequestHandler):
    def get(self):
        self.redirect('/saying')

def routing_test():
    parse_command_line()
    app = tornado.web.Application(
        handlers=[
            (r'/saying/?', SayingHandler),
            (r'/weather/([^/]{2,})/?', WeatherHandler),
            (r'/.+', ErrorHandler),
        ],
        template_path=os.path.join(os.path.dirname(__file__), 'templates')
    )
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    routing_test()