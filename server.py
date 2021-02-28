#!/usr/bin/python3

# Standard libraries only.
import socket

# Initialize socket bind variables with user input, hardcoded for testing.
# lhost = str(input("Local bind address\n"))
# lport = int(input("Local bind port\n"))
lhost = '127.0.0.1'
lport = 7002
lserver = (lhost, lport)

# Take a command from a user
cmd = input("What is your command\n")

# Establish server, and listen for a connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((lhost, lport))
s.listen()

# Accept a connection and send the command
(conn, addr) = s.accept()
print('connected by', addr)
conn.sendall(bytes(cmd, "utf-8"))