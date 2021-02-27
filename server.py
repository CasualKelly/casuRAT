#!/usr/bin/python3

# Standard libraries only.
import socket

# Initialize socket bind variables with user input.
LHOST = str(input("Local bind address\n"))
LPORT = int(input("Local bind port\n"))
LSERVER = (LHOST, LPORT)

# Create a socket that accepts connections, prints who connected, and recieves a message.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((LHOST, LPORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('connected by', addr)
        while True:
            DATA = conn.recv(1024)
            if not DATA:
                break
            print(DATA)