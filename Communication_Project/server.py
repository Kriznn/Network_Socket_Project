import socket
import os
import os.path

SERVERDATA = "serverData"

hostIP = socket.gethostbyname(socket.gethostname())
PORT = 4455     #this is the macro
ADDR = (hostIP, PORT)
SIZE = 1024     #this is the size of the bytes of the messages
FORMAT = "utf-8"       #This is needed in order to encode and decode messages between the client and the server.
parentDir = os.path.dirname(os.path.abspath(__file__))

def main():
    print("SERVER is starting")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #We just made the socket for the server.
    server.bind(ADDR)   #We bind out current address(hostIP and PORT #) to the server.
    server.listen()     #We are now listening to any signs from the client.

    print("SERVER is waiting for client")

    while True:
        connection, address = server.accept()      #This is the code for waiting for the client.
        print("New Connection from the client.py made")
        filename = connection.recv(SIZE).decode(FORMAT)     #This is the code that take the code given in the client.py
        print("Now getting the command from client.py")
        fileStuff = filename.split("/")
        #If this is the correct way to do it, make a loop here so that the server will take in multiple.
        file, text = fileStuff[0], fileStuff[1]

        newPath = os.path.join(parentDir, SERVERDATA)
        filePath = os.path.join(newPath, file)

        print(filePath)

        with open(filePath, 'w') as writeFile:
            writeFile.write(text)



main()