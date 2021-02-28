#!/usr/bin/python3

# Standard libraries only.
import socket

# Initialize socket bind variables with user input, hardcoded for testing.
lhost = str(input("Local bind address\n"))
lport = int(input("Local bind port\n"))
lserver = (lhost, lport)

# Take a command from a user
cmd = []
while True:
    cmdinput = str(input("Queue a command, or hit enter if done: "))
    if cmdinput:
        cmd.append(cmdinput)
        cmdinput = None
    else:
        break
print (cmd)

# Establish server, and listen for a connection.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((lhost, lport))
s.listen()

# Accept a connection, send the command, and receive the data.
(conn, addr) = s.accept()
with conn:
    print('connected by', addr)
    for c in cmd:
        print(c)
        conn.sendall(bytes((c), "utf-8"))
    while True:
        data = conn.recv(1024).decode()
        if not data:
            conn.close
            break
        print(data)