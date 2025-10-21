import os

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

produk = [
    {"nama": "Sofa", "harga": 75000, "stok": 10},
    {"nama": "Lampu Tidur", "harga": 125000, "stok": 5},
    {"nama": "Gantungan Kunci", "harga": 15000, "stok": 20}
]

pengguna = [
    {"username": "rega", "password": "123", "role": "admin"}
]

login_user = None

while True:
    clear()
    print("""
=========================================
|        TOKO AKSESORIS RUMAH           |
=========================================
| 1. Login                              |
| 2. Register                           |
| 3. Keluar                             |
=========================================
""")
    menu = input("Pilih menu (1-3): ")

    if menu == "2":
        clear()
        print("=== REGISTER PENGGUNA BARU ===")
        uname = input("Masukkan username baru: ")
        pw = input("Masukkan password: ")

        while True:
            role = input("Masukkan role (admin/user): ").lower()
            if role in ("admin", "user"):
                break
            else:
                print("Role tidak valid! Hanya boleh admin/user.")

        sudah_ada = False
        for p in pengguna:
            if p["username"] == uname:
                sudah_ada = True
                break

        if sudah_ada:
            print("Username sudah terdaftar!")
        elif uname == "" or pw == "":
            print("Input tidak boleh kosong!")
        else:
            pengguna.append({"username": uname, "password": pw, "role": role})
            print("Registrasi berhasil!")

        input("\nTekan Enter untuk kembali...")

    elif menu == "1":
        clear()
        if not pengguna:
            print("Belum ada pengguna terdaftar!")
            input("Tekan Enter...")
            continue

        print("=== LOGIN ===")
        uname = input("Username: ")
        pw = input("Password: ")

        login_user = None
        for p in pengguna:
            if p["username"] == uname and p["password"] == pw:
                login_user = p
                break

        if login_user is None:
            print("Login gagal! Username atau password salah.")
            input("\nTekan Enter untuk kembali...")
        else:
            print(f"Selamat datang, {login_user['username']}!")
            input("Tekan Enter...")

            if login_user["role"] == "admin":
                while True:
                    clear()
                    print("""
=========================
|       MENU ADMIN       |
=========================
| 1. Lihat Produk        |
| 2. Tambah Produk       |
| 3. Ubah Produk         |
| 4. Hapus Produk        |
| 5. Logout              |
=========================
""")
                    pilih = input("Pilih menu (1-5): ")

                    if pilih == "1":
                        clear()
                        print("============= DAFTAR PRODUK =============")
                        if not produk:
                            print("Belum ada produk.")
                        else:
                            print("No | Nama Produk    | Harga     | Stok")
                            print("-------------------------------------------")
                            for i, p in enumerate(produk, start=1):
                                print(f"{i}. {p['nama']:17} Rp{p['harga']:8}   {p['stok']}")
                        input("\nTekan Enter...")

                    elif pilih == "2":
                        clear()
                        print("=== TAMBAH PRODUK ===")
                        nama = input("Nama produk: ")
                        harga = input("Harga: ")
                        stok = input("Stok: ")

                        if nama == "" or not harga.isdigit() or not stok.isdigit():
                            print("Input tidak valid! Pastikan harga dan stok angka.")
                        else:
                            produk.append({"nama": nama, "harga": int(harga), "stok": int(stok)})
                            print("Produk berhasil ditambahkan!")
                        input("\nTekan Enter...")

                    elif pilih == "3":
                        clear()
                        print("======== UBAH PRODUK ========")
                        if not produk:
                            print("Belum ada produk untuk diubah.")
                        else:
                            for i, p in enumerate(produk, start=1):
                                print(f"{i}. {p['nama']} | Rp{p['harga']} | Stok: {p['stok']}")
                            pilih_ubah = input("\nMasukkan nomor produk: ")

                            if pilih_ubah.isdigit() and 1 <= int(pilih_ubah) <= len(produk):
                                idx = int(pilih_ubah) - 1
                                print(f"Data lama: {produk[idx]}")

                                nama = input("Nama baru: ")
                                harga = input("Harga baru: ")
                                stok = input("Stok baru: ")

                                if nama != "":
                                    produk[idx]["nama"] = nama
                                if harga.isdigit():
                                    produk[idx]["harga"] = int(harga)
                                if stok.isdigit():
                                    produk[idx]["stok"] = int(stok)

                                print("Data produk berhasil diubah!")
                            else:
                                print("Nomor tidak valid.")
                        input("\nTekan Enter...")

                    elif pilih == "4":
                        clear()
                        print("=== HAPUS PRODUK ===")
                        if not produk:
                            print("Belum ada produk untuk dihapus.")
                        else:
                            for i, p in enumerate(produk, start=1):
                                print(f"{i}. {p['nama']} | Rp{p['harga']} | Stok: {p['stok']}")
                            hapus = input("\nMasukkan nomor produk: ")

                            if hapus.isdigit() and 1 <= int(hapus) <= len(produk):
                                del produk[int(hapus) - 1]
                                print("Produk berhasil dihapus!")
                            else:
                                print("Nomor tidak valid.")
                        input("\nTekan Enter...")

                    elif pilih == "5":
                        login_user = None
                        break
                    else:
                        print("Pilihan tidak valid.")
                        input("Tekan Enter...")

            else:
                while True:
                    clear()
                    print(f"""
=========================
|       MENU USER        |
=========================
| 1. Lihat Produk        |
| 2. Logout              |
=========================
""")
                    pilih_user = input("Pilih menu (1-2): ")

                    if pilih_user == "1":
                        clear()
                        print("============= DAFTAR PRODUK =============")
                        if not produk:
                            print("Belum ada produk.")
                        else:
                            print("No | Nama Produk    | Harga      | Stok")
                            print("-------------------------------------------")
                            for i, p in enumerate(produk, start=1):
                                print(f"{i}. {p['nama']:17} Rp{p['harga']:8}   {p['stok']}")
                        input("\nTekan Enter...")

                    elif pilih_user == "2":
                        login_user = None
                        break
                    else:
                        print("Pilihan tidak valid.")
                        input("Tekan Enter...")

    elif menu == "3":
        print("Terima kasih telah menggunakan program ini.")
        break

    else:
        print("Pilihan tidak valid!")
        input("Tekan Enter...")