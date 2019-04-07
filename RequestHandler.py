from http.server import BaseHTTPRequestHandler, HTTPServer
from FileHandler import GetContents

httpd = None

class RequestHandler(BaseHTTPRequestHandler):
    # Utility function for sending headers and 200 response
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    # GET
    def do_GET(self):
        # Check path
        if self.path.startswith('/users'):
            response = GetContents('e:/Andrew Documents/etcpasswd.txt', self.path)
            ## print("Looking for users, eh?")
            self._set_headers()
            self.wfile.write(str(response).encode())
            return
        elif self.path.startswith('/groups'):
            ## print("Looking for groups? Me too")
            response = GetContents('e:/Andrew Documents/etcgroup.txt', self.path)
            self._set_headers()
            self.wfile.write(str(response).encode())
            return
        else:
            # otherwise return 404 not found
            self.send_response(404)
            self.end_headers()
            self.wfile.write('{"error": "invalid path"}'.encode())
        return

    # POST
    def do_POST(self):
        # This service does not support POST requests
        self.send_response(404)
        self.wfile.write('{"error": "POST Requests not allowed"}'.encode())
        return

def runHTTPService():
    global httpd
    if httpd is None:
        print("Starting server")
        httpd = HTTPServer(('localhost', 8000), RequestHandler)
        httpd.serve_forever()
        print("Server has shutdown")
    else:
        print("Server cannot be started because it is already running")
    return

def stopHTTPService():
    global httpd
    if httpd is None:
        print("Server cannot be stopped because it is not running")
        return
    print("Shutting down server")
    httpd.shutdown()
    httpd = None
