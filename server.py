#!/usr/bin/python3

# Standard libraries only.
import sys
import socket
import time
import pickle


# Take a command from a user, when no more input pickle up the list and break out.
def take_cmds():
    cmd_list = []
    while True:
        cmd_input = str(input("Queue a command, or hit enter if done: "))
        if cmd_input:
            cmd_list.append(cmd_input)
            cmd_input = None
        elif cmd_list:
            print (cmd_list, "\n")
            global dill_cmd
            dill_cmd = pickle.dumps(cmd_list)
            break
        else:
            print("no commands supplied")


def service_connection():
    with conn:
        print('Connection from', addr, "\n")
        conn.send(dill_cmd)
        while True:
            output = conn.recv(1024).decode()
            if not output:
                conn.close
                break
            utctime = time.asctime(time.gmtime())
            print(utctime, '|', addr[0], end=' | ')
            print(output)
            with open('casulog.txt','a') as log:
                log.write(utctime)
                log.write(" | ")
                log.write(addr[0])
                log.write(" | ")
                log.write(output)
                log.write(" \n")


if len(sys.argv) != 3:
    print("usage:", sys.argv[0], "<lhost> <lport>")
    sys.exit(1)


lhost, lport = sys.argv[1], int(sys.argv[2])
lserver = (lhost, lport)


while True:
    take_cmds()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(lserver)
    s.listen()
    (conn, addr) = s.accept()
    service_connection()
    s.shutdown
    s.close
    s = None