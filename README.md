# CasuRAT  
#### Simple python RAT for job interview and practice.  
  
casuRAT and it's partner server are ran entirely off of standard modules. As long as there is a somewhat updated version of python3, all that needs to be done is upload dbsetup.py & server.py to a server you control, upload casuRAT.py to targets, ensure they all have execute permissions, and run them with the below arguements.  
  
# Client Usage:  
#### python3 ./casuRAT_compiled.py [rhost] [rport] [beacon_interval_seconds]
  ##### rhost - The IP address of the C2 server
  ##### rport - Listening port of the C2 server
  ##### beacon_interval_seconds - The amount of time between attempts to communicate with the C2 server
  
Running casuRAT will start off with a prompt requesting user input on web proxy settings. Once the proxy chain has completed, casuRAT will make an initial attempt to reach out. Following a success or failure to connect, it will then sleep for the given time in seconds before attempting another connection. 

On a successful and authenticated connection, casuRAT will recieve a serialized list containing commands and parameters. It will run the commands on target, then return the stdout and stderr along with a simple timestamp/IP/command before each output to the server in a serialized object. As this is a proof of concept, below are statements the client prints to the terminal for troubleshooting. Real world application would have these error messages removed to cut down on strings.  
  
"Dad isn't home..." - No connection was established, most likely because the server is not active.  
"Dad hung up on me..." - A non-graceful reset occured while the connection was established.  
"Dad isn't speaking with me..." - Typically means the server is up, but not serving the client's specific IP. Triggered by a "refuse" string to prevent hanging.  
"Told dad all about $CMDS!" - Message confirming that commands were ran and sent off to the server.  
  
The client should ideally run indefinitely, and is at a decently stable place now.  


# sqlite3 Database initialization
#### python3 ./dbsetup.py
  
Running the DB setup will create casuRAT.db in the directory it ran from, and create a single table tailored to ingesting commands. Without the table, server.py will most likely throw an error.
  
  
# Server Usage  
#### python3 ./server.py [lhost] [lport] 
 ##### lhost - Designate the listening IP address  
 ##### lport - Designate the listening port  
   

Starting server.py will ask if you would like to query the database. This will display all entries. Pre-formatted options should come in the future.
  
Starting the server will prompt the user with a couple input trees that will take client IP addresses, and desired commands to be ran. The server will continue to run until all commands have been retrieved before exiting. If an address connects to the server that is not authorized to retrieve commands, a string "refused" will be sent and the socket will go back into it's listening state. A current limitation includes only holding two IPs/queues. Another limitation is that the server listens in a blocking state, meaning only one connection can be serviced at a time. Ensure that the waits on clients are staggered to not collide.  
  
The server will only exit once all command queues have been retrieved. Adding another queue requires restarting the script. ctrl+c while in listening mode should gracefully exit.  
  
  
  
# Requirements - Overall  
###### ~~Develop a remote access tool that provides arbitrary command execution~~  
  -casuRAT.py will run any system commands.  
###### ~~Deliver documentation outlining setup and use of the remote access tool~~   
  -Hello, I am the readme.  
  
# Requirements - Client  
###### ~~Run on Windows, Linux, or MacOS~~  
  -Runs on Linux with python3 installed. Potentially can run on other systems with python3, however not tested as of now.  
###### ~~Developed in Python 3~~  
  -Yup.  
###### ~~Use Python Modules in Standard Library only.~~  
  -No pip needed.  
###### ~~A mechanism to retrieve commands from the Server~~  
  -Uses basic socket receive call to retrieve commands. Try not to send too many commands at once since I have not allowed for over-buffer managements on command retrieval.  
###### ~~A mechanism to execute retrieved commands~~  
  -Uses the subprocess module to run commands. There are no limitations to number of arguments (within reason). As with any tool that is not interactive, do not run interactive commands. More, less, vi, etc. are all bad.  
###### ~~A mechanism to deliver the command results back to the server~~  
  -The same socket used for receiving the command will be used to send the stdout/stderr. The server buffer allows multiple chunks based on time hold. While in theory this should allow any amount of command output data sent to the server, every max buffer will add time to the connection. This can cause problems if another client attempts to retrieve commands at this time.  
  
# Requirements - Server  
###### ~~Run on Linux~~  
  -Runs on Linux with python3.  
###### ~~Developed in Python 3~~  
  -100% python 3.  
###### ~~Use only Python Modules in Standard Library~~  
  -No pip needed here.  
###### ~~A mechanism to queue tasks for clients~~  
  -A series of loops to queue commands for specific client IPs. The server will only provide these commands to their associated client IP.  
###### ~~A mechanism to deliver commands to a client.~~  
  -Our precious single socket hauling back and forth.  
###### ~~A mechanism to display results of a command returned by the client~~  
  -One the received packets are stitched back together they are printed to the terminal.  
###### ~~Long term storage of commands and subsequent results~~  
  -Currently the output that is displayed to the terminal is also written to a logfile titled "casulog.txt" that will be created in whatever directory the server is ran from. Below is an example of the output displayed to terminal and written to the log file.  
"""  
127.0.0.1  |  127.0.0.1 | Fri Mar  5 05:39:59 2021 | ls  
casulog.txt  
casuRAT.py  
LICENSE  
README.md  
server.py  
  
127.0.0.1 | Fri Mar  5 05:39:59 2021 | pwd  
/home/kelly/CasuRAT  
"""  
  
# Bonus - Client  
###### Develop a (second) compiled client (C/C++, Golang, C# etc)  
  -Maybe some day I'll get my hands dirty in C, but not today. Not satisfied.  
###### Leverage OOP  
  -Planning on restructuring code into classes to get true OOP experience. Not satisfied.  
###### ~~Obfuscate or encrypt client side code~~  
  -Compiled with py_compile. Obfuscates the client script into byte-code. Running strings against it will still give a strong indication of its purpose, but it is better than nothing.
###### ~~Obfuscate or encrypt command & control traffic~~  
  -Traffic in both directions is serialized into a pickled object. This encodes the traffic across the wire making it less obvious that someone is running commands on a target machine. Pickle may come with a security implication or two, so JSON dumps instead may be a better choice in the future.  
###### ~~Capable of traversing a web proxy.~~  
  -Found a seemingly simple solution through google, although I have not tested it in practice yet. Keep in mind that the communication between the client and server is not over HTTP(S), and will still try to directly connect to the server through whatever route is available. This should allow wgets, curls, and other web based commands such as package downloaders to traverse the web proxy. If I move from simple sockets and pickle to json/https in the future this will be much more valuable.
  
# Bonus - Server  
###### Leverage OOP  
  -Planning on restructuring code into classes to get true OOP experience. Not satisfied.  
###### ~~Configurable Server (Bind port/IP)~~  
  -Server ip/port is fed through terminal input upon running it.  
###### ~~Database Backend~~  
  -sqlite3 gave a very easy interface for interacting with a database file.
  
  
