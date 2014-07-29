import tornado.ioloop
import tornado.web
import tornado.httpserver
import tornado.websocket
import os
from jinja2 import Template

class MainHandler(tornado.web.RequestHandler):
    tpml = './index.html'
    content = './content.txt'
    def get(self):
        tpml = open(self.tpml, 'r').read()
        content = open(self.content, 'r').read().decode('utf-8')
        try:
            self.write(Template(tpml).render(content=content))
        except:
            import pdb; pdb.set_trace()

class WSHandler(tornado.websocket.WebSocketHandler):
    content = './content.txt'
    def open(self):
        print 'new connection'
        self.write_message("Hello World")
      
    def on_message(self, message):
        content = open(self.content, 'w')
        try:
            content.write(message.encode('utf-8'))
        except:
            import pdb; pdb.set_trace()
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
