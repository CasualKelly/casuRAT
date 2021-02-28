#!/usr/bin/python3

# Standard libraries only.
import subprocess

#Take user input and run command, return the stdout.
CMD = input("What is your command\n")
CMDARG = str(CMD).split(" ")
execute = subprocess.run(CMDARG, capture_output=True, text=True)
print("Command Ran:",CMD,"\n", execute.stdout)