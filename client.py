import socket
import sys

# Creating socket
cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
responseMessage = ""

# Connecting socket to server
try:
    cli_sock.connect((sys.argv[1], int(sys.argv[2])))
    responseMessage = str(cli_sock.getpeername()) + ": SUCCESS - connected to server. \n"

    # Send request back to server
    if sys.argv[3].lower() == "put" or sys.argv[3].lower() == "get":
        cli_sock.sendall(sys.argv[3].encode() + b' ' + sys.argv[4].encode())
    else:
        cli_sock.sendall(sys.argv[3].encode() + b' ')

except (ConnectionError, ConnectionAbortedError, ConnectionRefusedError):
    responseMessage = "FALIURE - couldn't connect to server. \n"

except Exception as e:
    responseMessage = "FAILURE - something has gone wrong. \n " + str(e)

finally:
    print(responseMessage)

    # Closing socket connection
    cli_sock.close()




