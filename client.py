#!/usr/bin/python3

# Standard libraries only
import socket

#initialize variables with hardcoded server address
RHOST = '172.16.100.133'
RPORT = 7001

#Create a socket object, connect to the server, and send a test message
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((RHOST, RPORT))
    s.sendall(b'Successful Test')
    data = s.recv(1024)

print('Test received', repr(data))