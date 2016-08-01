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
	  <img src="http://imgur.com/yIJIIVt.jpg" alt="slide1">
      <img src="http://imgur.com/FVqZi1Q.jpg" alt="slide2">
      <img src="http://imgur.com/Q6LszgW.jpg" alt="slide3">
      <img src="http://imgur.com/zl7AG29.jpg" alt="slide4">
      <img src="http://imgur.com/kMhGtMt.jpg" alt="slide5">
	  <img src="http://imgur.com/inJhoJ2.jpg" alt="slide5">
	  <img src="http://imgur.com/sVF426H.jpg" alt="slide5">
	  <img src="http://imgur.com/udQXNfA.jpg" alt="slide5">
	  <img src="http://imgur.com/8OTPIrZ.jpg" alt="slide5">
	  <img src="http://imgur.com/vFzDoXn.jpg" alt="slide5">
	  <img src="http://imgur.com/dbhr7CI.jpg" alt="slide5">
    </div>
</body>
				  </html>"""

if __name__ == "__main__":
    cherrypy.quickstart(Landing(), '/')