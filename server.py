import SimpleHTTPServer

class MyHTTPRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_my_headers()
        SimpleHTTPServer.SimpleHTTPRequestHandler.end_headers(self)

    def send_my_headers(self):
        self.send_header("Cache-Control", "public")
        self.send_header("Last-Modified", "Sat, 28 Jan 2017 07:28:00 GMT")
        self.send_header("Expires", "Sat, 4 Mar 2017 07:28:00 GMT")


if __name__ == '__main__':
    SimpleHTTPServer.test(HandlerClass=MyHTTPRequestHandler)