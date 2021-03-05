#!/usr/bin/python3

# Standard libraries only.
import sys
import socket
import time
import pickle


#if len(sys.argv) != 3:
#    print("usage:", sys.argv[0], "<lhost> <lport>")
#    sys.exit(1)
#
#
#lhost, lport = sys.argv[1], int(sys.argv[2])
#lserver = (lhost, lport)

lhost = "127.0.0.1"
lport = 7002
lserver = (lhost, lport)


dill_refuse = pickle.dumps("refused")
cmd_list = []
cmd_list2 = []


def take_cmds():
    cmd_input = str(input("What is the IP of the client: "))
    if cmd_input:
        cmd_list.append(cmd_input)
        cmd_input = None
        while True:
            cmd_input = (str(input("Queue a command, or hit enter if done: ")))
            if cmd_input:
                cmd_list.append(cmd_input)
                cmd_input = None
            elif len(cmd_list) >= 2:
                print (cmd_list, "\n")
                global dill_cmd
                dill_cmd = pickle.dumps(cmd_list[1:])
                return
            else:
                print("no commands supplied")
    else:
        print("I need a client IP cheif")
        sys.exit(1)


def take_cmds2():
        cmd_input2 = str(input("Additional client IP. If none, hit enter: "))
        if cmd_input2:
            cmd_list2.append(cmd_input2)
            cmd_input2 = None
            while True:
                cmd_input2 = str(input("Queue a command, or hit enter if done: "))
                if cmd_input2:
                    cmd_list2.append(cmd_input2)
                    cmd_input2 = None
                elif len(cmd_list2) >= 2:
                    print (cmd_list2, "\n")
                    global dill_cmd2
                    dill_cmd2 = pickle.dumps(cmd_list2[1:])
                    return
                else:
                    print("no commands supplied")
        else:
            print("All done, listening now...")
            return


def send_cmd(caddr, clist):
        print('Connection from', caddr, "\n")
        dill_cmd = pickle.dumps(clist[1:])
        conn.send(dill_cmd)


def return_cmds():
    while True:
        output = conn.recv(1024).decode()
        if not output:
            conn.close
            return
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

take_cmds()
take_cmds2()
while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(lserver)
    print("\nListening on", lserver)
    if cmd_list:
        print("Waiting to pass", cmd_list[1:], "to IP 1:", cmd_list[0])
    if cmd_list2:
        print("Waiting to pass", cmd_list2[1:], "to IP 2:", cmd_list2[0])
    s.listen()
    try:
        (conn, addr) = s.accept()
    except KeyboardInterrupt:
        sys.exit(1)
    else:
        if cmd_list:
            if addr[0] == cmd_list[0]:
                send_cmd(addr, cmd_list)
                return_cmds()
                cmd_list = []
            else:
                print(addr[0], "tried to connect, but was not", cmd_list[0])

        if cmd_list2:
            if addr[0] == cmd_list2[0]:
                send_cmd(addr, cmd_list2)
                return_cmds()
                cmd_list2 = []
            else:
                print(addr[0], "tried to connect, but was not", cmd_list2[0])
    conn.send(dill_refuse)
    s.close
    s = None