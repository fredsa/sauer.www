import jinja2
import os
import re
import webapp2

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

_REDIRECTS = {
    '/pda': 'https://sauer-pda.appspot.com/',
}

class MainHandler(webapp2.RequestHandler):

  def get(self):
    path_info = self.request.path_info

    url = _REDIRECTS.get(path_info, None)
    if url:
      return self.redirect(url)

    if path_info == '/robots.txt':
        self.response.status = 404
        return

    self.response.write('This page intentionally left blank.');

application = webapp2.WSGIApplication([
    ('/.*', MainHandler)
], debug=True)
