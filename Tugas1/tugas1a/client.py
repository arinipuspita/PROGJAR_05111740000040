import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print(f"connecting to {server_address}")
sock.connect(server_address)

# Send data
file = open("teks1.txt","rb")

try:
    while True:
        data = file.read(1024)
        print("file sedang dikirim....")
        if not data:
            break
        sock.send(data)
    print("file terkirim")
    file.close()

finally:
    print("selesai")
    sock.close()
