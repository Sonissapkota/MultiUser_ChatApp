import socket, threading

#Define constants to be used
host_ip = socket.gethostbyname(socket.gethostname())
host_port = 12345
encoder = "utf-8"
payload_length = 1024

#Create a server socket 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host_ip, host_port))
server_socket.listen()

#Creating a blank list to store connected clients socket and their names
client_sockets = []
client_names = []

def broadcast_message(message):
    for client in client_sockets:
        client.send(message)

def receive_message(client_socket):
    while True:
        try:
            message = client_socket.recv(payload_length)
            broadcast_message(message)
        except:
            index = client_socket
            client_sockets.remove(client_socket)
            client_socket.close()
            client_name = client_names[index]
            broadcast_message(f"{client_name} left the chat".encode(encoder))
            client_names.remove(client_name)
            break

def connect_client():
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connected with {client_address}")
        client_socket.send("NICKNAME".encode(encoder))
        client_name = client_socket.recv(payload_length).decode(encoder)
        client_sockets.append(client_socket)
        client_names.append(client_name)

        print(f"Client name is: {client_name}")
        broadcast_message(f"{client_name} joined the chat".encode(encoder))
        client_socket.send("Connected to the server".encode(encoder))

        t1 = threading.Thread(target=receive_message, args=(client_socket,))
        t1.start()

print("Server is listening")
connect_client()