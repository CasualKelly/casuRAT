# CasuRAT  
Simple python RAT for job interview and practice  
  
# Requirements - Overall  
Develop a remote access tool that provides arbitrary command execution  
Deliver documentation outlining setup and use of the remote access tool  
  
# Requirements - Client  
Run on Windows, Linux, or MacOS  
Developed in Python 3  
Use Python Modules in Standard Library only.  
A mechanism to retrieve commands from the Server  
A mechanism to execute retrieved commands  
A mechanism to deliver the command results back to the Server  
  
# Requirements - Server  
Run on Linux  
Developed in Python 3  
Use only Python Modules in Standard Library  
A mechanism to queue tasks for clients  
A mechanism to deliver commands to a client  
A mechanism to display results of a command returned by the client  
Long term storage of commands and subsequent results  
  
# Bonus - Client  
Develop a (second) compiled client (C/C++, Golang, C# etc)  
Leverage OOP  
Obfuscate or encrypt client side code  
Obfuscate or encrypt command & control traffic  
Capable of traversing a web proxy  
  
# Bonus - Server  
Leverage OOP  
Configurable Server (Bind port/IP)  
Database Backend  
  
# To-do list  
01. ~~Set up virtual machines for staging and testing (Kali --> Ubuntu)~~  
02. ~~Create a client and server that can connect to each other~~  
03. ~~Enable call back from client to server on an interval~~  
04. ~~Allow client to retrieve and run commands~~
05. Have client send results upon connecting to server, have server save to file  
06. Set up command queue on server that pushes all commands if correct IP connects  
07. Create interface that pulls command history and corresponding results  
08. ~~Create server interface allowing custom IP and port bind~~  
    a. Create arguements, help, and sanitization  
09. Implement some form of encryption (ssl?) between server and client  
10. Implement back end DB (nosql?) to store command, result, time, and client  
11. Objects?  
12. Web proxy?  
13. Do it all again in C# for the client
