import sys
import os
import socket
import logging
import json
from base64 import b64decode, b64encode

def list():
    data = {}
    data["perintah"] = 'list'
    massage = json.dumps(data)
    pkt_str = kirim_terima(massage)
    paket = json.loads(pkt_str)
    print(pkt_str)
    

def download(filename, simpan_nama):
    data = {}
    data["perintah"] = 'download'
    data['filename'] = filename
    massage = json.dumps(data)
    pkt_str = kirim_terima(massage)
    paket = json.loads(pkt_str)
    if(paket['respon']=='Berhasil'):
        print(f'saving file to {simpan_nama}')
        isi = b64decode(paket['isi'])
        f = open(simpan_nama, 'wb')
        f.write(isi)
        f.close()
        print(f'file {simpan_nama} berhasil disimpan ')


def upload(source, destination):
    data={}
    data["perintah"] = 'upload'
    data['filename'] = destination
    f = open(source, 'rb')
    raw_content = f.read()
    f.close()
    content = b64encode(raw_content)
    data['isi'] = content.decode()
    massage = json.dumps(data)
    pkt_str = kirim_terima(massage)
    paket = json.loads(pkt_str)
    print(f"RESPONS: {paket['respon']}")
    

def kirim_terima(massage):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logging.warning("membuka socket")

    server_address = ('localhost', 10000)
    logging.warning(f"opening socket {server_address}")
    sock.connect(server_address)

    try:
        logging.warning(f"CLIENT sending {massage}")
        sock.sendall(massage.encode())
        sock.shutdown(socket.SHUT_WR)
        
        # Look for the response
        paket = ''
        while True:
            data = sock.recv(64)
            if data:
                paket+=data.decode()
            else:
                break        
    finally:
        logging.warning("closing")
        sock.close()
    return paket
