import os
import socket
import common
import sys

# Creating socket
srv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Registering socket with OS ( defining IP and Port No. of endpoint )
srv_sock.bind(("", int(sys.argv[1])))

# Creating queue for incoming connection requests
srv_sock.listen(5)

while True:
    # Block until new incoming connection request
    # Return new socket connection to client and client address
    cli_sock, cli_addr = srv_sock.accept()

    # Receive the request
    request = cli_sock.recv(1024)
    requestStr = request.decode('utf-8').split(' ')
    requestType = requestStr[0]
    requestFileName = requestStr[1]

    serverFilePath = 'server_data/'
    clientFilePath = 'client_data/'

    # Processing the request
    if requestType == "PUT":
        clientFilePath += requestFileName
        requestFileData = common.readFile(cli_addr, clientFilePath)

        serverFilePath += requestFileName
        common.writeFile(cli_addr, serverFilePath, requestFileData)

    elif requestType == "GET":
        serverFilePath += requestFileName
        serverFileData = common.readFile(cli_addr, serverFilePath)

        clientFilePath += requestFileName
        common.writeFile(cli_addr, clientFilePath, serverFileData)

    elif requestType == "LIST":
        for entity in os.listdir():
            print(entity)

    else:
        print("Server can't deal with this request")

# Closing the socket connection
cli_sock.close()

