ukt = 6000000

nama = input("Masukkan Nama: ")
nim = input("Masukkan NIM: ")

nama_asli = "rega wahyu firenza"
nim_asli = "2509106085"

if nama == nama_asli and nim == nim_asli:
    print("Login berhasil!")
    print("1. Lunas (1%)")
    print("2. Cicilan 2x (5%)")
    print("3. Cicilan 4x (8%)")
    print("4. Cicilan 6x (12%)")

    pilihan = int(input("Pilih opsi pembayaran(1-4): "))

    if pilihan == 1:
        admin = 0.01
        total = ukt + (ukt * admin)
        print("Total yang harus dibayar: Rp",int(total))

    elif pilihan == 2:
        admin = 0.05
        total = ukt + (ukt * admin)
        cicilan = total / 2
        print("Total yang harus dibayar: Rp",int(total))
        print("Cicilan per periode: Rp",int(cicilan))

    elif pilihan == 3:
        admin = 0.08
        total = ukt + (ukt * admin)
        cicilan = total / 4
        print("Total yang harus dibayar: Rp",int(total))
        print("Cicilan per periode: Rp",int(cicilan))

    elif pilihan == 4:
        admin = 0.12
        total = ukt + (ukt * admin)
        cicilan = total / 6
        print("Total yang harus dibayar: Rp",int(total))
        print("Cicilan per periode: Rp",int(cicilan))

    else:print("Pilihan tidak tersedia.")
else:print("Login gagal! Nama atau NIM salah.")