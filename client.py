import socket, threading

#Define constant to be useed
destination_ip = socket.gethostbyname(socket.gethostname())
destination_port = 12345
encoder = 'utf-8'
payload_size = 1024

#Create a client socket
client_name = input("Enter your name:")
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((destination_ip, destination_port))

def send_message():
    while True:
        message = f'{client_name}: {input("")}'
        client_socket.send(message.encode(encoder))


def receive_message():
    while True:
        try:
            message = client_socket.recv(payload_size).decode(encoder)
            if message == "NICKNAME":
                client_socket.send(client_name.encode(encoder))
            else:
                print(message)
        except:
            print("An error occured!")
            client_socket.close()
            break

t1 = threading.Thread(target=send_message)
t1.start()

t2 = threading.Thread(target=receive_message)
t2.start()
