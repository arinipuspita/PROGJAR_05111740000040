import os
from base64 import b64decode, b64encode

class Files:
    def __init__(self, folder='./server'):
        self.root = folder
    
    def list_file(self):
        pipe = os.popen('dir ' + self.root,'r',64)
        hasil = pipe.read().split('\n')
        pipe.close()
        return hasil

    def download_file(self, filename):
        path = os.path.join(self.root, filename)
        if os.path.exists(path):
            file = open(path, 'rb')
            isi = file.read()
            file.close()
            hasil = b64encode(isi)
            return (True, hasil)
        else:
            return (False, hasil)

    def upload_file(self, filename, isi):
        path = os.path.join(self.root, filename)
        if os.path.exists(path):
            return False
        data = b64decode(isi)
        file = open(path, 'wb')
        file.write(data)
        file.close()
        return True

if __name__ == '__main__':
    d = Files() 
