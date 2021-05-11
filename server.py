import socket
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

    # Processing the request
    print(str(cli_addr) + ": " + request.decode('utf-8'))

    # Closing the socket connection
    cli_sock.close()
