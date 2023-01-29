import socket
import threading

# data handler function
def handle_client(c):
    # wait for incoming packet
    request = c.recv(1024).decode()

    # manipulate incoming text stream
    response = request + " from server xyz"

    # return the combined string to the client
    c.send(response.encode())
    print(f"Reply to {address[0]}:{address[1]}")

    # close socket
    c.close()

# create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(f"Socket created")

# define port
port = 8080

# bind socket to port
s.bind(("0.0.0.0", port))
print(f"Successfully bind to port:{str(port)}")

# listen for incoming connection
s.listen(5)
print("[*] Waiting for client")

# accept connection
while True:
    c, address = s.accept()
    print(f"Accepted connection from {address[0]}:{address[1]}")

    # fork and multithread
    client_handler = threading.Thread(target=handle_client, args=(c,))
    client_handler.start()
