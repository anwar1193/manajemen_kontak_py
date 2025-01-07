# Program Manajemen Kontak

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
        # melihat semua kontak
        if kontak:
            for num, item in enumerate(kontak, start=1):
                print(f"\n{num}. {item['nama']} ({item['HP']}, {item['email']})")
        else:
            print("\nKontak masih kosong")

    elif pilihan == '2':
        # menambahkan kontak
        nama = input("Masukkan Nama Kontak : ")
        HP = input("Masukkan Nomor HP : ")
        email = input("Masukkan Email : ")
        kontak_baru = {'nama' : nama, 'HP' : HP, 'email' : email}
        kontak.append(kontak_baru)
        print("Kontak baru berhasil ditambahkan!")

    elif pilihan == '3':
        # menghapus kontak
        print("\n")
        if kontak:
            for num, item in enumerate(kontak, start=1):
                print(f"{num}. {item['nama']} ({item['HP']}, {item['email']})")
        else:
            print("Kontak masih kosong!")
            continue

        i_hapus = int(input("Masukan nomor kontak yang akan dihapus : "))
        del kontak[i_hapus-1]
        print("Kontak Berhasil Dihapus")

    elif pilihan == '4':
        # keluar dari kontak
        break
    else:
        print("Anda memasukan pilihan yang salah")