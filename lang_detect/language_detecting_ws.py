#!/usr/bin/env python

"""
Program to implement language detection using the wsgiservice framework

Author: Cesar C. Desales (cesar@cesarcd.com)
Version: 0.01
Updated: 22/01/2012
Dependencies: wsgiservice (http://packages.python.org/WsgiService/)
Runs on: Python 2.6

How to run it: 
	python language_detecting_ws.py
	
How to test it:

	- POST method
		wget --header "Accept: application/json" --header "Content-Type: application/x-www-form-urlencoded"  --post-data="text=Hello+world.+Has+the+sun+risen+on+you+today%3F" --server-response -qO- http://localhost:8001/language_processor/
		
		Sample output:
		
		  HTTP/1.0 200 OK
		  Date: Sun, 22 Jan 2012 19:51:52 GMT
		  Server: WSGIServer/0.1 Python/2.6.5
		  Vary: Accept
		  Content-Length: 24
		  Content-Type: application/json; charset=UTF-8
		  Content-MD5: b68203ffb1dd45877c2d6dea5f6c4230
		"{\"language\": \"ge\"}"
		
	- GET method. Not implemented as of this version
		wget --header "Accept: application/json" --server-response -qO- http://localhost:8001/language_processor/
"""

import random

from wsgiservice import (
	mount,
	get_app,
	Resource,
)

class LanguageDetector(object):
    """Basic dummy implementation of a 
    Language Detection component"""
    
    def detect(self, text):
        return random.choice(("en", "es", "de", "fr", "ge", "it"))

class ResponseDataBuilder(object):
    """Basic class to build a response data structure"""
    def build(self, text):
        return dict(language = text)

@mount("/language_processor/")
class LanguageDetectorFrontend(Resource):
    """Web service to do language processing tasks"""
    
    detector = LanguageDetector() 
    resp_builder = ResponseDataBuilder()
    
    def POST(self, text):
        """Return language detected from input text."""
        lang = self.detector.detect(text)
        data = self.resp_builder.build(lang)
        self.set_response_content_type()
        return self.to_application_json( data )
    
    def GET(self, id):
        #Not Implemented. TODO: Implement
        raise_404(self)

    def PUT(self, id):
        #Not Implemented. TODO: Implement
        raise_404(self)

    def DELETE(self, id):
        #Not Implemented. TODO: Implement
        raise_404(self)

app = get_app(globals())

def run_server():
    from wsgiref.simple_server import make_server
    print "Running on port 8001"
    make_server('', 8001, app).serve_forever()
    
if __name__ == '__main__':
    run_server()