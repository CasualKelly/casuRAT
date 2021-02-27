#!/usr/bin/python3

# Standard libraries only
import socket

# Initialize remote host variables with user input
RHOST = str(input("C2 IP Address\n" ))
RPORT = int(input("C2 Port\n"))
RSERVER = (RHOST, RPORT)

# Simple input collection
DATA = str(input("What would you like to say?\n" ))

# Connect out
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(RSERVER)
s.sendall(bytes(DATA,"utf-8"))