import config
from tornado import web, httpserver, ioloop
import json
import main

class answerHandle(web.RequestHandler):
    def get(self, *args, **kwargs):

        text =json.loads(self.get_argument('problem'))
        
        course_name=self.get_argument('coursename')
        #course_name = ' '
        
        #print(course_name)
        #print(text)

        #print(main.handleData(text))

        self.write('success_jsonpCallback('+json.dumps(main.handleData(text,course_name))+')')

application = web.Application([
    (r"/getAnswer",answerHandle),
])

if __name__ == "__main__":
    print('lunch success!')
    http_server = httpserver.HTTPServer(application)
    http_server.listen(config.Set['port'])
    ioloop.IOLoop.current().start()


