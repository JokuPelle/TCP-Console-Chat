import socket
import select
import threading
import sys

#AF_INET = Address domain (ipv4), SOCK_STREAM means data is read continuosly (socket type TCP)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostname(), 1234))
server.listen(5)

while True:
    clientsocket, address = server.accept()
    print(f"Connection from {address} has been established!")
    clientsocket.send(bytes("Welcome to the server", "utf-8"))