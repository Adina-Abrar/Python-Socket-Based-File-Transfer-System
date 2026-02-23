import socket
import os

SERVER_IP = '127.0.0.1'
SERVER_PORT = 5001
BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"

filename = "file_to_send.txt"
filesize = os.path.getsize(filename)
header = f"{filename}{SEPARATOR}{filesize}".ljust(128)  # fixed 128-byte header

client_socket = socket.socket()
client_socket.connect((SERVER_IP, SERVER_PORT))
client_socket.send(header.encode())

with open(filename, "rb") as f:
    while True:
        bytes_read = f.read(BUFFER_SIZE)
        if not bytes_read:
            break
        client_socket.sendall(bytes_read)

print(f"[+] File {filename} sent successfully to server")
client_socket.close()
