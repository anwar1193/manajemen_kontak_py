# Program Manajemen Kontak

def melihat_kontak():
    # melihat semua kontak
    if kontak:
        for num, item in enumerate(kontak, start=1):
            print(f"\n{num}. {item['nama']} ({item['HP']}, {item['email']})")
    else:
        print("\nKontak masih kosong")
        return 99

def menambah_kontak():
    # menambahkan kontak
    nama = input("Masukkan Nama Kontak : ")
    HP = input("Masukkan Nomor HP : ")
    email = input("Masukkan Email : ")
    kontak_baru = {'nama': nama, 'HP': HP, 'email': email}
    kontak.append(kontak_baru)
    print("Kontak baru berhasil ditambahkan!")

def menghapus_kontak():
    # menghapus kontak
    if melihat_kontak() == 99:
        return
    else:
        i_hapus = int(input("Masukan nomor kontak yang akan dihapus : "))
        del kontak[i_hapus - 1]
        print("Kontak Berhasil Dihapus")


kontak1 = {'nama' : 'Anwar', 'HP' : '085219063505', 'email' : 'anwar@mail.com'}
kontak2 = {'nama' : 'Shinta', 'HP' : '08521984990', 'email' : 'shinta@mail.com'}
kontak = [kontak1, kontak2]

while True:
    print("\nMenu Kontak")
    print("1. Melihat Semua Kontak")
    print("2. Menambahkan Kontak Baru")
    print("3. Menghapus Kontak")
    print("4. Keluar Dari Kontak")

    pilihan = input("Masukkan pilihan menu kontak (1, 2, 3 atau 4) : ")

    if pilihan == '1':
        melihat_kontak()

    elif pilihan == '2':
        menambah_kontak()

    elif pilihan == '3':
        menghapus_kontak()

    elif pilihan == '4':
        # keluar dari kontak
        break
    else:
        print("Anda memasukan pilihan yang salah")