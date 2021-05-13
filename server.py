import common
import socket
import sys

# Creating socket
srv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Registering socket with OS ( defining IP and Port No. of endpoint )
srv_sock.bind(("", int(sys.argv[1])))

# Creating queue for incoming connection requests
srv_sock.listen(5)

while True:
    try:
        # Block until new incoming connection request
        # Return new socket connection to client and client address
        cli_sock, cli_address = srv_sock.accept()
        responseMessage = str(cli_address)

        # Receive the request
        request = cli_sock.recv(1024)
        requestStr = request.decode('utf-8').split(' ')
        requestType = requestStr[0].lower()
        requestFileName = requestStr[1]

        serverFilePath = 'server_data/'
        clientFilePath = 'client_data/'

        # Processing the request
        if requestType == "put":
            clientFilePath += requestFileName
            requestFileData = common.readFile(responseMessage, clientFilePath)

            if requestFileData is not None:
                serverFilePath += requestFileName
                common.writeFile(responseMessage, serverFilePath, requestFileData)

        elif requestType == "get":
            serverFilePath += requestFileName
            serverFileData = common.readFile(responseMessage, serverFilePath)

            if serverFileData is not None:
                clientFilePath += requestFileName
                common.writeFile(responseMessage, clientFilePath, serverFileData)

        elif requestType == "list":
            common.listDirectoryContents(responseMessage)

        else:
            print("Server can't deal with this request. \n")

        # Closing the socket connection
        cli_sock.close()
    except KeyboardInterrupt:
        break


