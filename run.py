#!/usr/bin/python3

# Standard libraries only.
import subprocess

# Run commands on host, return results.
CMD = input("What is your command\n")
CMDARG = str(CMD).split(" ")
subprocess.run(CMDARG)

# POC, will be pushed into the connection later.
print("completed", CMD)
