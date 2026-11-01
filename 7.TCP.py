import socket
import threading

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", 5000))
    server_socket.listen(1)

    conn, addr = server_socket.accept()
    print("Client connected:", addr)

    message = conn.recv(1024).decode()
    print("Message from client:", message)

    response = "Hello Client, message received!"
    conn.send(response.encode())

    conn.close()
    server_socket.close()


# Start server
server_thread = threading.Thread(target=server)
server_thread.start()

# Create client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 5000))

message = input("Enter message: ")
client_socket.send(message.encode())

response = client_socket.recv(1024).decode()
print("Response from server:", response)

client_socket.close()
server_thread.join()
