import socket
import threading

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(("127.0.0.1", 5000))

    message, address = server_socket.recvfrom(1024)
    print("Message from client:", message.decode())

    response = "Hello Client, message received!"
    server_socket.sendto(response.encode(), address)

    server_socket.close()


# Start server
server_thread = threading.Thread(target=server)
server_thread.start()

# Create client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = input("Enter message: ")

# Send message to server
client_socket.sendto(message.encode(), ("127.0.0.1", 5000))

# Receive response
response, address = client_socket.recvfrom(1024)
print("Response from server:", response.decode())

client_socket.close()
server_thread.join()
