Apa saja yang bisa dilakukan :
1. Meletakkan file (upload)
2. Mengambil file (download)
3. Melihat list file (list)

Dokumentasi protokol :
1. upload : untuk meletakkan file 
   request : upload 
   parameter : source destination 
   response: berhasil -> berhasil gagal -> File sudah tersedia
2. download : untuk mengambil file 
   request : download 
   parameter: filename, nama yang akan disimpan 
   response: berhasil -> berhasil gagal -> File tidak ditemukan
3. list : untuk list file pada direktori tertentu 
   request : list 
   parameter : tidak ada 
   response : berhasil -> berhasil

Apabila perinta tidak dikenali maka program akan memberi respon "Perintah Tidak Ditemukan"
