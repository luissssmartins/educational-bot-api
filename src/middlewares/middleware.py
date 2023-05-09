from werkzeug.wrappers import Request, Response, ResponseStream

import os

class Middleware:

    def __init__(self, app):
        self.app = app
        self.api_key = os.getenv('API_KEY')
    
    def __call__(self, environ, start_response):
        request = Request(environ)

        api_key = request.authorization['api_key']

        if api_key == self.api_key:
            environ['api_key'] = { 'api_key': api_key }

            return self.app(environ, start_response)
        
        res = Response(u'Autorização falhou', mimetype='text/plain', status=401)

        return res(environ, start_response)