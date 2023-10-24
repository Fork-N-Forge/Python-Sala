# chat_client.py

import socket
import sys
import select

HOST = '127.0.0.1' 
PORT = 12345

my_username = input("Username: ")

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# Connect to the server
s.connect((HOST, PORT))

while 1:
    
    socket_list = [sys.stdin, s]
    
    # Get the list sockets which are readable
    read_sockets, write_sockets, error_sockets = select.select(socket_list , [], [])
    
    for sock in read_sockets:
        if sock == s:
            # incoming message from remote server, s
            data = sock.recv(2048)
            if not data :
                print('\nDisconnected from chat server')
                sys.exit()
            else :
                #print data
                sys.stdout.write(data)
        
        else :
            # user entered a message
            msg = sys.stdin.readline()
            s.send(my_username + ": " + msg)
            sys.stdout.write("<You>")
            sys.stdout.write(msg)
            sys.stdout.flush() 

s.close()