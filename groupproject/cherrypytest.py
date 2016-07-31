import cherrypy

class Landing(object):		
    @cherrypy.expose
    def index(self):
        return """<html>
		<!DOCTYPE html>
					<head>
    <title>
    CherryPy project for COSC 1336
    </title>
</head>
<body>
<link rel="stylesheet" type="text/css" href="theme.css">
    <h1 style='align:center'>CherryPy</h1>
    <div class="boxitem">
        <h3 id = "team">The Team:</h3>
Davis Richardson, Brett Piatek, Malorie Lara and Marla Boeer are Novice computer scientists with interests ranging from web design to robotics. This project - implementing the web framework module CherryPy - allowed them to bring their interests together in order to present a workable example of what this module is capable of; its strengths and limitations.
    </div>
    <div class = "boxitem">
      <h3>CherryPy:</h3>
      <img src="http://i.imgur.com/kMhGtMt.png
                " alt="slide1">
      <img src="" alt="slide2">
      <img src="" alt="slide3">
      <img src="" alt="slide4">
      <img src="" alt="slide5">
    </div>
</body>
				  </html>"""

if __name__ == "__main__":
    cherrypy.quickstart(Landing(), '/')