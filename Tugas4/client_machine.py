import json
import base64
from files import Files

class Client_machine:
    def __init__(self):
        self.files = Files()
    
    def run(self, json_proses):
        objek = json.loads(json_proses)
        massage = {}
        try:
            perintah = objek['perintah']
            if perintah == 'list':
                massage['list'] = self.files.list_file()
                respon = 'Berhasil'
            elif perintah == 'upload':
                filename = objek['filename']
                data = objek['isi']
                isi = data.encode()
                ret_val = self.files.upload_file(filename, isi)
                respon = 'Berhasil' if ret_val else 'File sudah tersedia'
            elif perintah == 'download':
                filename = objek['filename']
                ret_val, binary = self.files.download_file(filename)
                isi = binary.decode()
                massage['isi'] = isi
                respon = 'Berhasil' if ret_val else 'File tidak ditemukan'
            else:
                respon = 'Perintah salah'
        except:
          print(e.what())
          respon = 'ERROR'
        finally:
            massage['respon'] = respon
            return json.dumps(massage)
if __name__=='__main__':
    cm = Client_machine()
