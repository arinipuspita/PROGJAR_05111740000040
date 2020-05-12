from socket import *
import socket
import threading
import time
import sys

from client_machine import Client_machine

class ProcessTheClient(threading.Thread):
    def __init__(self, connection, address):
        self.connection = connection
        self.address = address
        self.client_machine = Client_machine()
        threading.Thread.__init__(self)

    def run(self):
        massage = ''
        while True:
            data = self.connection.recv(64)
            if data:
                massage += data.decode()
                print(massage)
            else:
                break
        hasil = self.client_machine.run(massage)
        print(hasil)
        self.connection.sendall(hasil.encode())
        print('sukses send')
        self.connection.close()
        
class Server(threading.Thread):
    def __init__(self):
        self.the_clients = []
        self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        threading.Thread.__init__(self)

    def run(self):
        self.my_socket.bind(('0.0.0.0', 10000))
        self.my_socket.listen(1)
        while True:
            self.connection, self.client_address = self.my_socket.accept()

            clt = ProcessTheClient(self.connection, self.client_address)
            clt.start()
            self.the_clients.append(clt)


def main():
    svr = Server()
    svr.start()
    print('mencari koneksi')


if __name__ == "__main__":
    main()
