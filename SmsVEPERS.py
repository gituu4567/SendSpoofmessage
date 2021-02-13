#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from os import system as s



banner = """
                                  
                                  
.       ..---..--. .---..--.  .-. 
 \     / |    |   )|    |   )(   )
  \   /  |--- |--' |--- |--'  `-. 
   \ /   |    |    |    |  \ (   )
    '    '---''    '---''   ` `-' 
                                  
                                  
                                                                                                              
                                                                                                                                
| You have the right to send a message to the phone address you want once a day. 
| Your message has a limited number of characters, you will see this after you write your message.
| You may get an error if you do not enter your phone address correctly.
| This tool was created by @vepers in Turkish language exclusively for THT members & was edited and translated into English language by hash30 a.k.a anonymous.
| Please note that you can't send any type of links included in the message body. This tool was not created for spamming anyone or misuse.

"""

print(banner)

import datetime
now = datetime.datetime.now()
print ("Current date and time: ")
print (now.strftime("%d-%m-%Y %H:%M:%S"))

import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)

sor = input("Phone number Ex:+905555555555 >>> ")

message = input("Your message >>> ")

arlk = message[0:70]

print("\n| The part of your message that can be sent is as follows.\n"+arlk)

drlm = input("\n| Send Your Message?[y/n] >>> ")

if drlm == "y" or drlm == "Y":
    print("\n"+sor+"\n"+arlk+"\n")
    resp = requests.post('https://textbelt.com/text', {
  'phone': sor,
  'message': arlk,
  'key': 'textbelt',
    })
    print(resp.json())

elif drlm == "n" or drlm == "N":
    quit()
else:
    print("\n|You made a mistake.")

