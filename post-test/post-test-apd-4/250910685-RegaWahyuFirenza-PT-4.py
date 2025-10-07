print("=== SELAMAT DATANG DI TOKO FURNITUR INFORDEH ===")

username_benar = "Rega"
password_benar = "2509106085"
percobaan = 0

while percobaan < 3:
    username = input("Masukkan Username (Nama): ")
    password = input("Masukkan Password (NIM): ")

    if username == username_benar and password == password_benar:
        print("\nLogim Berhasil! Selamat Datang,",username)
        break
    else:
        percobaan += 1
        sisa = 3 - percobaan
        print("Login Gagal.Sisa Percobaan:", sisa)
        if percobaan == 3:
            print("Login Gagal 3 Kali.Program Berhenti.")
            exit()

while True:
    print("\n====== MENU PEMBELIAN FURNITUR ======")
    print("1. Sofa                 - Rp 500.000")
    print("2. Meja Belajar         - Rp 250.000")
    print("3. Rak Lemari           - Rp 150.000")
    print("4. Keluar")            

    pilihan = input("Pilih Opsi (1-4): ")

    if pilihan == "4":
        print("Terima Kasih Telah Berbelanja!")
        break
    elif pilihan == "1":
        jenis = "Sofa"
        harga = 500000
    elif pilihan == "2":
        jenis = "Meja Belajar"
        harga = 250000
    elif pilihan == "3":
        jenis = "Rak Lemari"
        harga = 150000
    else:
        print("Pilihan Tidak Valid! Silahkan Coba Lagi.")
        continue

    jumlah = input(f"Masukkan jumlah {jenis} yang ingin dibeli: ")

    if jumlah.isdigit():
        jumlah = int(jumlah)
        total_bayar = 0

        for i in range(jumlah):
            total_bayar += harga

        if total_bayar >= 700000:
            potongan = total_bayar * 0.20
            total_akhir = total_bayar - potongan
            bonus = "Diskon 20%"
        elif total_bayar >= 500000:
            potongan = total_bayar * 0.8
            total_akhir = total_bayar - potongan
            bonus = "Diskon 8%"
        elif total_bayar >= 150000:
            potongan = total_bayar
            total_akhir = total_bayar - potongan
            bonus = "Kitchen Set"
        else:
            total_akhir = total_bayar
            bonus = "Tidak Ada"

        print("\n======= STRUK PEMBELIAN =======")
        print("Jenis Furnitur     :", jenis)
        print("Jumlah Unit        :", jumlah)
        print("Total_Bayar        : Rp",int(total_bayar))
        print("Bonus/Diskon       :", bonus)
        print("=============================")

    else:
        print("Input jumlah harus berupa angka!")