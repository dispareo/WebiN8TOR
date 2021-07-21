# WebiN8TOR
#Web reconnaissance tool that puts together multiple web app tools
#Still in development


#!/usr/bin/python3
import subprocesses
import sys
import socket
import pyfiglet

banner = pyfiglet.figlet_format("WebiN8TOR")
print(banner)

if len(sys.argv) !=2:
  raise ValueError("Please provide an IP to target")
  
host = sys.argv[1]
ports = [80,443,8000,8080]
  
print("Starting enumeration... \n\nPreparing World Domination... \n\n Or maybe just a lil' pwnage")


try:
  for x in ports:
  s = s.socket.socket(socket_AF_INET, socket.SOCK_STREAM)
  result = s.connect_ex((host,x))
    if result ==0:
            print("Port {} is open, let's enumerate further".format(x))
        s.close()  
