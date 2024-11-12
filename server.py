from http.server import BaseHTTPRequestHandler, HTTPServer

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        message = "Hello, World! Here is a GET response"
        self.wfile.write(bytes(message, "utf8"))
        print(self.request)
        
        
        
        
        
        
        
        
    def do_POST(self):
        
        
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()


        print(content_length)
        print(post_data.decode())
        file1 = open("log.txt", "w") 
        file1.write(post_data.decode())
        file1.close() 

with HTTPServer(('', 8080), handler) as server:
    server.serve_forever()