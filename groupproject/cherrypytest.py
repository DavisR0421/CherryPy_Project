import cherrypy

class Landing(object):		
    @cherrypy.expose
    def index(self):
        return """
		<html>
			<div id="slideshow">
			<div>
				<img src="//farm6.static.flickr.com/5224/5658667829_2bb7d42a9c_m.jpg">
			</div>
			<div>
				<img src="//farm6.static.flickr.com/5230/5638093881_a791e4f819_m.jpg">
			</div>
			<div>
				Pretty cool eh? This slide is proof the content can be anything.
			</div>
			</div>
		</html>"""

if __name__ == "__main__":
    cherrypy.quickstart(Landing(), '/')