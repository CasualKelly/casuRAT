#!/usr/bin/python3

# Standard libraries only.
import socket
import time
import pickle

# Initialize socket bind variables with user input, hardcoded for testing.
lhost = str(input("Local bind address: "))
lport = int(input("Local bind port: "))
lserver = (lhost, lport)

# Take a command from a user, when no more input pickle up the list and break out
cmd_list = []
while True:
    cmd_input = str(input("Queue a command, or hit enter if done: "))
    if cmd_input:
        cmd_list.append(cmd_input)
        cmd_input = None
    else:
        print (cmd_list, "\n")
        dill_cmd = pickle.dumps(cmd_list)
        break

# Establish server, and listen for a connection.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((lhost, lport))
s.listen()

# Accept a connection, send the command, and receive the data.
(conn, addr) = s.accept()
with conn:
    print('Connection from', addr, "\n")
    conn.send(dill_cmd)
    while True:
        output = conn.recv(1024).decode()
        if not output:
            conn.close
            break
        print(addr, end=': ')
        print(output)
