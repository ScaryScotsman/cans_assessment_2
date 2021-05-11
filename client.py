import socket
import sys

# Creating socket
cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connecting socket to server
cli_sock.connect((sys.argv[1], int(sys.argv[2])))

# Send request back to server
cli_sock.sendall(sys.argv[3].encode('utf-8'))

# Closing socket connection
cli_sock.close()
