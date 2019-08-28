#Akshy Palanisamy server python program
#This program is the server program for the chat


from socket import *
import sys
from threading import Thread



#This try and except makes sure that the user providea a valid port number in arg[1]
try:
    portNum = int(sys.argv[1])
except (IndexError):
    print("Please provide a valid port number, ex: python3 server.py 43500")
    sys.exit()

#This while loop makes sure that the port number is within a valid range
while portNum<43500 or 43505<portNum:
    portNum = int(input("Please provide a valid port number between 43500-43505: "))

#setup socket to wait for clients
serverPort = portNum
serverSocket = socket(AF_INET, SOCK_STREAM) #TCP (reliable)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) #make port reusable
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to accept clients')

#array to hold the clients that join
clients = []


#This function takes in the client socket and recieves messages
#Then sends the message to all the clients in the client array
def msgSendRecv(sock):
    while True: #continue to take in messages from clients
        sentenceFromClient = sock.recv(1024).decode("utf-8")
        for connectionSocket, addr in clients:
            connectionSocket.send(sentenceFromClient.encode("utf-8"))

#This while statement continually accepts new clients and appends them to the 
#client array then creates a new thread for each client to send and recieve message 
#throught the msgSendRecv function
while True:
    connectionSocket, addr = serverSocket.accept()
    clients.append((connectionSocket, addr))
    Thread(target=msgSendRecv, args=(connectionSocket,)).start()



#closing the socket
serverSocket.close()


