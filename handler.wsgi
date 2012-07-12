import sys
import viriatum_wsgi

MESSAGE = "My Own Hello World!"
""" The message to be printed """

def application(environ, start_response):
      """
      Simplest possible application object
      """

      print viriatum_wsgi.VERSION
      print viriatum_wsgi.input
      _input = viriatum_wsgi.input()
      _input = environ["wsgi.input"]
      a = _input.read()
      a = str(sys.path)
      
      content_length = len(a)
      status = "200 OK"
      response_headers = [
          ("Content-Type", "text/plain"),
          ("Content-Length", str(content_length))
      ]
      write = start_response(status, response_headers)
      return [a]
