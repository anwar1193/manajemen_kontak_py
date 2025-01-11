# Program Manajemen Kontak

class Kontak:
    def __init__(self):
        self.kontak = []

    def melihat_kontak(self):
        # melihat semua kontak
        if self.kontak:
            for num, item in enumerate(self.kontak, start=1):
                print(f"\n{num}. {item['nama']} ({item['HP']}, {item['email']})")
        else:
            print("\nKontak masih kosong")
            return 99

    def menambah_kontak(self):
        # menambahkan kontak
        nama = input("Masukkan Nama Kontak : ")
        HP = input("Masukkan Nomor HP : ")
        email = input("Masukkan Email : ")
        kontak_baru = {'nama': nama, 'HP': HP, 'email': email}
        self.kontak.append(kontak_baru)
        print("Kontak baru berhasil ditambahkan!")

    def menghapus_kontak(self):
        # menghapus kontak
        if self.melihat_kontak() == 99:
            return
        else:
            i_hapus = int(input("Masukan nomor kontak yang akan dihapus : "))
            del self.kontak[i_hapus - 1]
            print("Kontak Berhasil Dihapus")


kontak_kantor = Kontak()
# kontak_keluarga = Kontak()


while True:
    print("\nMenu Kontak")
    print("1. Melihat Semua Kontak")
    print("2. Menambahkan Kontak Baru")
    print("3. Menghapus Kontak")
    print("4. Keluar Dari Kontak")

    pilihan = input("Masukkan pilihan menu kontak (1, 2, 3 atau 4) : ")

    if pilihan == '1':
        kontak_kantor.melihat_kontak()

    elif pilihan == '2':
        kontak_kantor.menambah_kontak()

    elif pilihan == '3':
        kontak_kantor.menghapus_kontak()

    elif pilihan == '4':
        # keluar dari kontak
        break
    else:
        print("Anda memasukan pilihan yang salah")