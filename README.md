# Client-Chat program

This client-chat program was written in the python programming language and runs on the linux terminal.

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
To exit the client program enter the command '/shutdown'.
