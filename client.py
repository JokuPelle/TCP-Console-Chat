import socket
import select
import errno
import sys
HEADER_LENGHT = 10
IP = "127.0.0.1"
PORT = 1234
#***********************
# TCP socket chat client
#***********************

print("""Welcome!
Private message users by starting your message with @[username]
Leave the server by typing -exit-""")
my_username = input("Username: ")
my_channel = input("Enter channel (1-4): ")
my_username = my_channel+my_username

#Establish the connection to server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))
client_socket.setblocking(False)

username = my_username.encode('utf-8')
username_header = f"{len(username):<{HEADER_LENGHT}}".encode('utf-8')
client_socket.send(username_header + username)

while True:
    #Send messages
    message = input(f"{my_username[1:]}> " )#Input blocks incoming message stream. GUI could fix this
    if "-exit-" in message:
        print("Exiting the server.")
        break
    if message:
        message = message.encode('utf-8')
        message_header = f"{len(message):<{HEADER_LENGHT}}".encode('utf-8')
        client_socket.send(message_header + message)
    
    # Recieve messages
    try:
        while True:
            username_header = client_socket.recv(HEADER_LENGHT)
            if not len(username_header):
                print("Connection closed by server.")
                sys.exit()
            username_length = int(username_header.decode('utf-8').strip())
            username = client_socket.recv(username_length).decode('utf-8')

            message_header = client_socket.recv(HEADER_LENGHT)
            message_length = int(message_header.decode('utf-8').strip())
            message = client_socket.recv(message_length).decode('utf-8')
            if message.find("@") == 0:
                if message.find(my_username[1:]) == 1:
                    print(f"{username[1:]}> {message}")
            else:
                print(f"{username[1:]}> {message}")

    except IOError as e:
        #Error when no more messages incoming (these errors should happen)
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print("Reading error", str(e))
            sys.exit()
        continue

    except Exception as e:
        print("General error", str(e))
        sys.exit()