#!/usr/bin/python3

# Standard libraries only.
import socket

# Initialize socket bind variables with user input.
# LHOST = str(input("Local bind address\n"))
LHOST = '127.0.0.1'
# LPORT = int(input("Local bind port\n"))
LPORT = 7001
LSERVER = (LHOST, LPORT)

# Create a socket that accepts connections, prints who connected, and recieves a message.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((LHOST, LPORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('connected by', addr)
        while True:
            DATA = conn.recv(1024).decode()
            if not DATA:
                break
            print(DATA)