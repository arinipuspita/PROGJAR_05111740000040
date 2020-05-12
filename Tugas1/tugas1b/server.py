import sys
import socket
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('127.0.0.1', 20000)
print(f"memulai dari {server_address}")
sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)
while True:
    # Wait for a connection
    print("menunggu koneksi")
    connection, client_address = sock.accept()
    print(f"koneksi dari {client_address}")
    # Receive the data in small chunks and retransmit it
    request = connection.recv(1024)
    file = open(request.decode(),"rb")
    print("request diterima")
    while True:
        data = file.read(1024)
        if not data:
            break
        connection.sendall(data)
        print("mengirimkan.....")
    # Clean up the connection
    file.close()
    connection.close()