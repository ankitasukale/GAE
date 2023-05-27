import webapp2
class Mainpage(webapp2.RequestHandler):
    def get(self):
        self.response.write("hello world")
    app=webapp2.WSGIApplication([('/',Mainpage)],debug=true)