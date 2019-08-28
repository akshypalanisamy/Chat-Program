Client-Chat program
Created by Akshy Palanisamy

This client-chat programs runs on the linux terminal.
The program was tested on the Ubunutu terminal.

Features:
+The program takes in hostname and port number through command line arguments.
+Clients can send/recieve messages at any time in any order.
+The program works with arbitrary number of clients.
+Client can specify a hostname instead of an IP address.
+Client can enter the command /shutdown to exit the program.
+Client/Server can work with arbitrary length messages while ensuring that entire message is sent and recieved.

Below are the instructions to run the program:

    Open the terminal and first run the server:

        $python3 server.py 43500

    Then open a new terminal and run the client:

        $python3 client.py localhost 43500

Enter a user name of your choosing when prompted by the client program.
To add more clients just open a new terminal and run the client program again to add a new client.
To exit the client program enter the command '/shutdown'

-----------------------------------------------------------------------------------------------------------------------
