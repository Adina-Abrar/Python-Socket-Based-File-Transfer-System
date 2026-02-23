import socket
import threading
import os
import sys

SERVER_IP = '0.0.0.0'
SERVER_PORT = 5001
BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"

def handle_client(client_socket, address):
    print(f"[+] {address} connected.")
    received = client_socket.recv(128).decode().strip()  # fixed 128-byte header
    try:
        filename, filesize = received.split(SEPARATOR)
        filename = os.path.basename(filename)
        filename = f"received_{address[1]}_{filename}"
        filesize = int(filesize)
    except Exception as e:
        print(f"[!] Error parsing header from {address}: {received}")
        client_socket.close()
        return

    with open(filename, "wb") as f:
        bytes_read = 0
        while bytes_read < filesize:
            data = client_socket.recv(BUFFER_SIZE)
            if not data:
                break
            f.write(data)
            bytes_read += len(data)
            progress = (bytes_read / filesize) * 100
            sys.stdout.write(f"\r[+] Receiving {filename} from {address}: {progress:.2f}%")
            sys.stdout.flush()
    print(f"\n[+] File received successfully from {address}: {filename}")
    client_socket.close()

server_socket = socket.socket()
server_socket.bind((SERVER_IP, SERVER_PORT))
server_socket.listen(5)
print(f"[+] Server listening on {SERVER_IP}:{SERVER_PORT}")

while True:
    client_socket, address = server_socket.accept()
    thread = threading.Thread(target=handle_client, args=(client_socket, address))
    thread.start()
