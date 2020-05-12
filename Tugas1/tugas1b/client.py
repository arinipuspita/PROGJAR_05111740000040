import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 20000)
print(f"menyambungkan ke {server_address}")
sock.connect(server_address)

try:
    # Send data
    message = 'teks1.txt'
    print(f"mengirim request")
    sock.sendall(message.encode())
    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    file = open("teks2.txt","wb")
    
    while True:    
        if amount_received < amount_expected:  
            data = sock.recv(1024)        
            amount_received += len(data)
            file.write(data)
            print("file diterima")
        else:
            break
    file.close()
finally:
    print("selesai")
    sock.close()
