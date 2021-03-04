#!/usr/bin/python3

# Standard libraries only.
import sys
import socket
import time
import pickle


# Take a command from a user, when no more input pickle up the list and break out.
def take_cmds():
    cmd_list = []
    cmd_input = str(input("What is the IP of the client: "))
    if cmd_input:
        cmd_list.append(cmd_input)
        cmd_input = None
        while True:
            cmd_input = (str(input("Queue a command, or hit enter if done: ")))
            if cmd_input:
                cmd_list.append(cmd_input)
                cmd_input = None
            elif cmd_list[1]:
                print (cmd_list, "\n")
                global dill_cmd
                dill_cmd = pickle.dumps(cmd_list[1:])
                break
            else:
                print("no commands supplied")
    else:
        print("I need a client IP cheif")
        sys.exit(1)

# Take second IP from user.
    while True:
        cmd_list2 = []
        cmd_input2 = str(input("Additional client IP. If none, hit enter: "))
        if cmd_input2:
            while True:
                cmd_input2 = str(input("Queue a command, or hit enter if done: "))
                if cmd_input2:
                    cmd_list2.append(cmd_input2)
                    cmd_input2 = None
                elif cmd_list2:
                    print (cmd_list2, "\n")
                    global dill_cmd2
                    dill_cmd2 = pickle.dumps(cmd_list2)
                    break
                else:
                    print("no commands supplied")
        else:
            print("All done, listening now...")
            return


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