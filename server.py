import tornado.ioloop
import tornado.web
import tornado.httpserver
import tornado.websocket
import os
from jinja2 import Template

path = os.path.dirname(__file__)
static_path = path
tpml = path+'/index.html'
content = path+'/content.txt'

class MainHandler(tornado.web.RequestHandler):
    tpml = path+'/index.html'
    content = path+'/content.txt'
    def get(self):
        tpml = open(self.tpml, 'r')
        content = open(self.content, 'r')
        self.write(Template(tpml.read()).render(content=content.read()))

class WSHandler(tornado.websocket.WebSocketHandler):
    content = path+'/content.txt'
    def open(self):
        print 'new connection'
        self.write_message("Hello World")
      
    def on_message(self, message):
        print 'message received %s' % message
        content = open(self.content, 'w')
        content.write(message)
        content.close()

 
    def on_close(self):
      print 'connection closed'



application = tornado.web.Application([
    (r"/", MainHandler),
    (r'/ws', WSHandler)
])

if __name__ == "__main__":
    
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
