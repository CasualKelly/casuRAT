#!/usr/bin/python3

# Standard libraries only.
import socket
import time

# Initialize socket bind variables with user input.
# lhost = str(input("Local bind address\n"))
# lport = int(input("Local bind port\n"))
lhost = '127.0.0.1'
lport = 7002
lserver = (lhost, lport)

# Take a command from a user
cmd = input("What is your command\n")

# Create a socket that accepts connections, prints who connected, and recieves a message.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((lhost, lport))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('connected by', addr)
        while True:
            conn.sendall(bytes(cmd, "utf-8"))
            break
            if not cmd:
                break