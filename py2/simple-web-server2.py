#!/usr/bin/env python
"""
Very simple HTTP server in python2.x.
Usage::
    ./simple-web-server2.py [<port>]
Send a GET request::
    curl http://localhost:8080
Send a HEAD request::
    curl -I http://localhost:8080
Send a POST request::
    curl -d "foo=bar&bin=baz" http://localhost:8080
"""
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import datetime


class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.protocol_version = self.request_version
        self.send_response(200)
    #   self.send_header('Content-type', 'text/html')
    #   self.send_header('Content-type', 'application/json')
        self.end_headers()

    def _print_request_header(self):
        d = datetime.datetime.today()
        print'================================================================================'
        print d, self.client_address
        print self.requestline
        print
        print self.headers

    def _do_redirect(self, location='http://localhost:8080/redirect'):
        if self.path.startswith('/redirect'):
            self._set_headers()
        else:
            redirect_path = '/redirect' + self.path
            location = 'http://127.0.0.1:8080{0}'.format(redirect_path)
            self.protocol_version = self.request_version
            self.send_response(301)
            self.send_header('Location', location)  # e.g. 'http://www.google.co.jp'
            self.end_headers()

    def do_GET(self):
        self._print_request_header()
        self._set_headers()
    #   self._do_redirect()
    #   self.wfile.write("<html><body><h1>HTTP Get</h1></body></html>")

    def do_HEAD(self):
        self._print_request_header()
        self._set_headers()

    def do_POST(self):
        # Doesn't do anything with posted data
        self._print_request_header()
        if 'Content-Length' in self.headers :
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            print post_data
        self._set_headers()


def run(server_class=HTTPServer, handler_class=S, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print 'Sopping httpd...'


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
