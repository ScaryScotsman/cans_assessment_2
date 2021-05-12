import socket
import sys

# Creating socket
cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connecting socket to server
cli_sock.connect((sys.argv[1], int(sys.argv[2])))

# Send request back to server
cli_sock.send(sys.argv[3].encode() + b' ')

if sys.argv[3] == "PUT" or sys.argv[3] == "GET":
    cli_sock.send(sys.argv[4].encode())

# Closing socket connection
cli_sock.close()
