import socket
import sys
import os
import os.path

clientIP = socket.gethostbyname(socket.gethostname())
PORT = 4455
ADDR = (clientIP, PORT)
FORMAT = "utf-8"
SIZE = 1024
parentDir = os.path.dirname(os.path.abspath(__file__))

def main():
    print(f"Command line arguments: {sys.argv[1]}")
    clientFolder = sys.argv[1]
    concurrentTimes = int(sys.argv[2])
    tempNum = concurrentTimes
    value = 0
    print("Client is starting")
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    print("Successfully connected to the server.")
    #We are now going to open the folder

    clientPath = os.path.join(parentDir, clientFolder)

    while tempNum != 0:
        client_list = os.path.join(clientPath, f"example{value}.txt")
        fileOpen = open(client_list, 'w')
        fileOpen.write("Hello my Name is Chris")
        # print(f"test: {client_list}")
        tempNum-=1
        value+=1


    value = 0
    tempNum = concurrentTimes

    client_list_new = os.listdir(clientPath)

    while tempNum != 0:
        newClientPath = os.path.join(clientPath, client_list_new[value])
        file = open(str(newClientPath), "r")
        text = file.read()

        dataToSend = (f"{client_list_new[value]}/{text}")
        
        client.send(dataToSend.encode(FORMAT))

        value+=1
        tempNum -=1
    # while value != 3:
    #     file = open(f"clientData/textFile{value}.txt", "x")
    #     value += 1

    # client.send(f"textFile1.txt".encode(FORMAT))

main()

