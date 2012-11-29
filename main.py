import jinja2
import os
import re
import webapp2

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

_REDIRECTS = {
    '/': '/about',
    '/pda': 'https://sauer-pda.appspot.com/',
    '/com.allen_sauer.gwt.game.hornetblast.HornetBlast/HornetBlast.html': 'http://hornet-blast.appspot.com/',
    '/com.allen_sauer.gwt.voices.demo.VoicesDemo/VoicesDemo.html': 'https://gwt-voices.appspot.com/',
    '/com.allen_sauer.gwt.dnd.demo.DragDropDemo/DragDropDemo.html': 'https://gwt-dnd.appspot.com/',
    '/com.allen_sauer.gwt.dnd.demo.DragAndDropDemo/DragAndDropDemo.html': 'https://gwt-dnd.appspot.com/',
    '/com.allen_sauer.gwt.log.demo.LogDemo/LogDemo.html': 'https://gwt-log.appspot.com/',
}

class MainHandler(webapp2.RequestHandler):

  def get(self):
    path_info = self.request.path_info

    url = _REDIRECTS.get(path_info, None)
    if url:
      return self.redirect(url)

    if not path_info.endswith('/'):
      return self.redirect('{0}/'.format(path_info))

    template = jinja_environment.get_template('site/page.html')
    values = {
        'content': '{0}/content.html'.format(self.request.path_info),
    }
    try:
      html = template.render(values)
    except:
      return self.redirect('/')

    self.response.write(html)

application = webapp2.WSGIApplication([
    ('/.*', MainHandler)
], debug=True)
