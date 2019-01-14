# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 15:33:16 2018

@author: adam
"""

import telnetlib
import getpass
try:
    #get host and password
    host = input("Enter Host : ")
    password = getpass.getpass()
    #set port number
    port = 8080
    #set timeout 30 seconds
    timeout = 30
    #create telnet obj and connect to host
    tn = telnetlib.Telnet(host,port,timeout)
    #enter password when asked
    tn.read_until("Password: ")
    tn.write(password+ "\n")
    #enter enable mode]
    tn.write("enable\n")
    #open config.txt read 
    f = open("config.txt", "r")
    for x in f:
        tn.write(x + "\n")
    f.close()
except:
    print("Sorry something went wrong please enter correct info and try again")
