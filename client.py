import socket

SERVER_HOST = '192.168.1.1'   # replace with actual server IP
SERVER_PORT = 13337           

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_HOST, SERVER_PORT))

while True:
    message = input("Enter your message: ")
    client.send(bytes(message, 'utf-8'))
    response = client.recv(1024).decode('utf-8')
    print("Person B:", response)

client.close()