# chat_server.py

import socket
import select


socket_list = []

users = {}

def broadcast(server_socket, sock, message):
    for socket in socket_list:
        if socket != server_socket and socket != sock :
            try :
                socket.send(message)
            except :
                
                socket.close()
                socket_list.remove(socket)

if __name__ == "__main__":

   
    HOST = '127.0.0.1'  

    
    PORT = 12345

  
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 

  
    server_socket.bind((HOST, PORT))                                

    # Now wait for client connection.
    server_socket.listen(5)

    # Add server socket object to the list of readable connections
    socket_list.append(server_socket)

    print("Chat server started on port " + str(PORT))

    while 1:

        # Get the list sockets which are ready to be read through select
        # 4th arg, time_out  = 0 : poll and never block
        ready_to_read,ready_to_write,in_error = select.select(socket_list,[],[],0)
      
        for sock in ready_to_read:
            # a new connection request recieved
            if sock == server_socket: 
                sockfd, addr = server_socket.accept()
                socket_list.append(sockfd)
                print("Client (%s, %s) connected" % addr)
                
                broadcast(server_socket, sockfd, "[%s:%s] entered room\n" % addr)
             
            # a message from a client, not a new connection        
            else:
                # process data recieved from client, 
                try:
                    # receiving data from the socket.
                    data = sock.recv(2048)
                    if data:
                        broadcast(server_socket, sock, "\r" + '[' + str(sock.getpeername()) + '] ' + data)  
                    else:
                        # remove the socket that's broken    
                        if sock in socket_list:
                            socket_list.remove(sock)

                        # at this stage, no data means probably the connection has been broken
                        broadcast(server_socket, sock, "Client (%s, %s) is offline\n" % addr) 

                # exception 
                except:
                    broadcast(server_socket, sock, "Client (%s, %s) is offline\n" % addr)
                    continue

    server_socket.close()