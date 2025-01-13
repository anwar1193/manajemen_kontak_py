'Berisi kelas kontak untuk menjalankan program kontak'

import fungsi

class Kontak:
    def __init__(self):
        self.kontak = fungsi.membuka_kontak()

    def melihat_kontak(self):
        # melihat semua kontak
        if self.kontak:
            for num, item in enumerate(self.kontak, start=1):
                print(f"{num}. " + item)
        else:
            print("\nKontak masih kosong")
            return 99

    def menambah_kontak(self):
        # menambahkan kontak
        nama = input("Masukkan Nama Kontak : ")
        HP = input("Masukkan Nomor HP : ")
        email = input("Masukkan Email : ")
        kontak_baru = f'{nama} {HP}, {email}' + '\n'
        self.kontak.append(kontak_baru)
        print("Kontak baru berhasil ditambahkan!")

    def menghapus_kontak(self):
        # menghapus kontak
        if self.melihat_kontak() == 99:
            return
        else:
            try:
                i_hapus = int(input("Masukan nomor kontak yang akan dihapus : "))
                del self.kontak[i_hapus - 1]
                print("Kontak Berhasil Dihapus")
            except:
                print("Input yang anda masukan salah!!")

    def keluar_kontak(self):
        fungsi.menyimpan_kontak(isi=self.kontak)