import socket
import threading
import os

SERVER_IP = '127.0.0.1'
SERVER_PORT = 5002
BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"
FILENAME = "file_to_send.txt"

clients = []

def handle_client(client_socket, address):
    print(f"[+] {address} connected.")
    clients.append(client_socket)

server_socket = socket.socket()
server_socket.bind((SERVER_IP, SERVER_PORT))
server_socket.listen(5)
print(f"[+] Server listening on {SERVER_IP}:{SERVER_PORT}")

# Accept clients
accepting_thread = threading.Thread(target=lambda: [handle_client(*server_socket.accept()) for _ in iter(int, 1)])
accepting_thread.start()

input("Press Enter to send the file to all clients...\n")

filesize = os.path.getsize(FILENAME)
for client in clients:
    client.send(f"{FILENAME}{SEPARATOR}{filesize}".encode())
    with open(FILENAME, "rb") as f:
        while True:
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                break
            client.sendall(bytes_read)
    print(f"[+] Sent {FILENAME} to {client.getpeername()}")
