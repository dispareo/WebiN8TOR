# WebiN8TOR
#Web reconnaissance tool that puts together multiple web app tools
#Still in development


#!/usr/bin/python3
import subprocesses
import sys
import socket

host = sys.argv[1]
ports = [80,443,8000,8080]

if len(sys.argv) !=2:
  raise ValueError("Please provide an IP to target")
  
print("Starting enumeration... \n\nPreparing World Domination... \n\n Or maybe just a lil' pwnage")

for x in ports:
  s = s.socket.socket(socket(AF_INET, socket.SOCK_STREAM)
  result = s.connect_ex((host,x))
    if result == 0:
                      print(f"Port {x} is open, we'll enumerate that...")
  
