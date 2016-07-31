import cherrypy

class Landing(object):		
    @cherrypy.expose
    def index(self):
        return """<html>
					<img src="http://blogs-images.forbes.com/insertcoin/files/2015/07/zelda.png" style = "width:200px; height:300px;">
				  </html>"""

if __name__ == "__main__":
    cherrypy.quickstart(Landing(), '/')