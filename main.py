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

    if path_info.endswith('.html'):
        # return
        template = jinja_environment.get_template('site' + path_info)
        values = {
        }
    else:
        if not path_info.endswith('/'):
          return self.redirect('{0}/'.format(path_info))

        template = jinja_environment.get_template('site/page.html')
        values = {
            'content': '{0}/content.html'.format(self.request.path_info),
        }

    html = template.render(values)
    try:
        html = template.render(values)
    except Exception, e:
        raise e
        # return self.redirect('/')

    self.response.write(html)

application = webapp2.WSGIApplication([
    ('/.*', MainHandler)
], debug=True)
