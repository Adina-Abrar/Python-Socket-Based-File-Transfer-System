import socket
import os

SERVER_IP = '127.0.0.1'  # replace with server's local IP
SERVER_PORT = 5002
BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"

client_socket = socket.socket()
client_socket.connect((SERVER_IP, SERVER_PORT))

received = client_socket.recv(BUFFER_SIZE).decode()
filename, filesize = received.split(SEPARATOR)
filename = f"received_{filename}"
filesize = int(filesize)

with open(filename, "wb") as f:
    bytes_read = 0
    while bytes_read < filesize:
        data = client_socket.recv(BUFFER_SIZE)
        if not data:
            break
        f.write(data)
        bytes_read += len(data)
        progress = (bytes_read / filesize) * 100
        print(f"\r[+] Receiving {filename}: {progress:.2f}%", end="")
print(f"\n[+] File received successfully: {filename}")
client_socket.close()
