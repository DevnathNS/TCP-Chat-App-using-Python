import socket
import threading

HOST = '192.168.1.1'          # replace with actual client IP
PORT = 13337                

def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break
     
        print("Person A:", data)
    
        response = input("Enter your response: ")
        client_socket.send(bytes(response, 'utf-8'))
        client_socket.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    
    print(f"[*] Listening on {HOST}:{PORT}")
    
    while True:
        client, addr = server.accept()
        print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")
        client_handler = threading.Thread(target=handle_client,
        args=(client,))
        client_handler.start()

if __name__ == "__main__":
    main()