#Akshy Palanisamy client python program
#This program is the client program for the chat
#This program can be run multiple times to add more clients

from socket import *
import sys
import fcntl
import os
import select
from threading import Thread


#This try and except makes sure that user provides a server hostmane in arg[1]
try:
    hostname = sys.argv[1]
except (IndexError):
    print("Please provide a valid server hostname and port, ex:python3 client.py localhost 43500")
    sys.exit()

#This try and except makes sure that user provides a port number in arg[2]
try:
    portNum = int(sys.argv[2])
except (IndexError):
    print("Please provide a valid port number")
    sys.exit()

#This while statement makes sure that the user provides a port number between the valid range
while portNum<43500 or 43505<portNum:
    portNum = int(input("Please provide a valid port number between 43500-43505: "))


#Getting the user's name for the chat
userName = input("Please provide a username:")

#Creating the TCP socket and connecting it to the port and server 
serverName = hostname
serverPort = portNum
clientSocket = socket(AF_INET, SOCK_STREAM) #TCP socket
clientSocket.connect((serverName, serverPort))

#Sending the user's name to alert the people in the chat that a new user has joined
clientSocket.send((userName+" has joined the chat!").encode('utf-8'))

#Telling the user that to exit they can use the command '/shutdown'
print("To exit use the command '/shutdown'")

#The recv function that will run as a sperate thread so that the messages 
#can be recieved while getting the user's input
def recv():
    while True: #while statement that continuously recieves messages
        #The try and except statement is catches an exception if there is an error
        try:
            messageFromServer = clientSocket.recv(2048).decode('utf-8')
            print("\n"+messageFromServer) #printing the message from the server to the terminal
            sys.stdout.write("Send: ")#Signifier for the user to type the message to send
            sys.stdout.flush()#flusing the stdout
        except OSError:
            break


#starting a seperate thread for the recv funciton so that the user can provide
#input while recieving messages from the server
recvThread = Thread(target=recv)
recvThread.start()


#This while statement continously takes user input and sends the message to the server
while True:
    messageToServer = input() #getting user input
     #if statement to check if the user has eneterd thec command to exit the chat
     #then send the message that the user has left and exit the program
    if(messageToServer == "/shutdown"):
        clientSocket.send((userName+" has left the chat!").encode('utf-8'))
        clientSocket.close()
        exit()
    else: #otherwise continue recieving messages from the server
        clientSocket.send((userName+": "+messageToServer).encode('utf-8'))


 #closing the socket
clientSocket.close()




    


