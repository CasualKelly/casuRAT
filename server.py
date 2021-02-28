#!/usr/bin/python3

# Standard libraries only.
import socket

# Initialize socket bind variables with user input.
# lhost = str(input("Local bind address\n"))
lhost = '127.0.0.1'
# lport = int(input("Local bind port\n"))
lport = 7001
lserver = (lhost, lport)

# Create a socket that accepts connections, prints who connected, and recieves a message.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((lhost, lport))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('connected by', addr)
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            print(data)