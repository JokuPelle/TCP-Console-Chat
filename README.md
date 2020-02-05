# TCP Socket Chat Room
Simple chat room that utilizes TCP socket technology. Made for Distributed Systems course.

## Disclaimer
app.py is just a small test for a GUI and isn't connected to the main program.

## Running
First you need to start the server. Both the server and clients run on localhost.

The server doens't have a command to stop it, so you need to close the program manually.
```
python server.py
```

Then you can start as many clients as you want.
```
python client.py
```
Once your client has logged into the server, you can disconnect and close the program by typing "-exit-" as your message.

## Features
* The client logs in with their IP address and enters a username and the channel they want to enter.
* Only users on the same channel can see your messages.
* You can private message users by typing "@[username]" at the start of your message. Only they can see your message
(if they are on the same channel).
* You can exit the server and close the client by typing "-exit-" as your message.

## Problems
The client side message input blocks the constant message stream, so the client only sees new messages when they send a new message.
A GUI could fix this. Currently you can quickly refresh by leaving no message (just press enter).
