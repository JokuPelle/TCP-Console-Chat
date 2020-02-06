import socket
import select
HEADER_LENGHT = 10
IP = "127.0.0.1"
PORT = 1234
#***********************
# TCP socket chat server
#***********************

#Create a socket with address domain (ipv4) and make it read data constantly (TCP)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#Binds socket to address
server_socket.bind((IP, PORT))
server_socket.listen()

sockets_list = [server_socket]
clients = {}
print("Server started!")

#Used for establishing a connectiona and recieving messages
def recieve_message(client_socket):
    try:
        message_header = client_socket.recv(HEADER_LENGHT)
        if not len(message_header):
            return False
        message_length = int(message_header.decode('utf-8').strip())
        return {"header": message_header, "data": client_socket.recv(message_length)}
    except:
        return False

while True:
    #Read, write and exeption sockets
    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)
    for notified_socket in read_sockets:
        #Access to server
        if notified_socket == server_socket:
            client_socket, client_address = server_socket.accept() #client_address is [hostaddr, port]

            user = recieve_message(client_socket)
            if user is False:
                continue
            sockets_list.append(client_socket)
            clients[client_socket] = user
            print(f"Accepted new connection from {client_address[0]}:{client_address[1]} username: {user['data'].decode('utf-8')}!")
        #Message to server
        else:
            message = recieve_message(notified_socket)
            if message is False:
                print(f"Closed connection from {clients[notified_socket]['data'].decode('utf-8')}")
                sockets_list.remove(notified_socket)
                del clients[notified_socket]
                continue
            user = clients[notified_socket]
            print(f"Recieved message from {user['data'].decode('utf-8')}: {message['data'].decode('utf-8')}")

            #Send message to clients
            for client_socket in clients:
                #Do not send message back to sender and only to the same channel
                if client_socket != notified_socket and clients[client_socket]['data'].decode('utf-8')[0] == user['data'].decode('utf-8')[0]:
                    #print("same channel")
                    client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])
    
    #Precausion for exception sockets
    for notified_socket in exception_sockets:
        sockets_list.remove(notified_socket)
        del clients[notified_socket]