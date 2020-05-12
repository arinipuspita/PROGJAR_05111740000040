import threading
import time
import datetime
import logging
import requests
import os


def download_photo(url=None, i=None):
    if (url is None):
        return False
    ff = requests.get(url)
    tipe = dict()
    tipe['image/png'] = 'png'
    tipe['image/jpg'] = 'jpg'
    tipe['image/jpeg'] = 'jpg'

    content_type = ff.headers['Content-Type']
    # logging.warning(content_type)
    if (content_type in list(tipe.keys())):
        namafile = os.path.basename(url)
        ekstensi = tipe[content_type]
        # logging.warning(f"writing {namafile}.{ekstensi}")
        fp = open(f"Photo{i}.{ekstensi}", "wb")
        fp.write(ff.content)
        fp.close()
    else:
        return False


if __name__ == '__main__':
    url_download = [
        'https://i.pinimg.com/originals/83/5c/cf/835ccf272d23da0609db055a29bddb08.jpg',
        'https://i.pinimg.com/originals/77/58/51/775851c1765e438a482d38783858f0ea.jpg']

    threads = []
    i = 1
    for url in url_download:
        t = threading.Thread(target=download_photo, args=(url, i,))
        threads.append(t)
        i += 1

    for thr in threads:
        thr.start()
