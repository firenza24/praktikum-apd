import os

produk = [
    {"nama": "Sofa", "harga": 75000, "stok": 10},
    {"nama": "Lampu Tidur", "harga": 125000, "stok": 5},
    {"nama": "Gantungan Kunci", "harga": 15000, "stok": 20}
]

pengguna = [
    {"username": "rega", "password": "123", "role": "admin"}
]

login_user = None

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def hitung_total(harga, jumlah):
    return harga * jumlah

def cari_produk(nama_produk):
    for p in produk:
        if p["nama"].lower() == nama_produk.lower():
            return p
    return None

def menu_utama():
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
    try:
        menu = input("Pilih menu (1-3): ")
        if menu == "1":
            login()
        elif menu == "2":
            registrasi()
        elif menu == "3":
            print("Terima kasih telah menggunakan program ini.")
            exit()
        else:
            raise ValueError("Menu tidak valid!")
    except ValueError as e:
        print("Error:", e)
        input("Tekan Enter...")
        menu_utama()
    finally:
        print("Kembali ke menu utama...")

def registrasi():
    global pengguna
    clear()
    print("=== REGISTER PENGGUNA BARU ===")
    uname = input("Masukkan username baru: ").strip()
    pw = input("Masukkan password (minimal 3 angka): ").strip()
    try:
        if not uname or not pw:
            raise ValueError("Username dan password tidak boleh kosong!")
        if len(pw) < 3:
            raise ValueError("Password minimal 3 karakter!")
        if not pw.isdigit():
            raise ValueError("Password hanya boleh angka!")
    except ValueError as e:
        print(e)
        input("Tekan Enter...")
        return
    for p in pengguna:
        if p["username"] == uname:
            print("Username sudah terdaftar!")
            input("Tekan Enter...")
            return
    pengguna.append({"username": uname, "password": pw, "role": "user"})
    print("Registrasi berhasil!")
    input("Tekan Enter untuk kembali...")
    menu_utama()

def login():
    global login_user
    clear()
    print("=== LOGIN ===")
    uname = input("Username: ")
    pw = input("Password: ")
    try:
        user = next(p for p in pengguna if p["username"] == uname and p["password"] == pw)
        login_user = user
        print(f"Selamat datang, {uname}!")
        input("Tekan Enter...")
        if user["role"] == "admin":
            menu_admin()
        else:
            menu_user()
    except StopIteration:
        print("Login gagal! Username atau password salah.")
        input("Tekan Enter...")
        menu_utama()

def tampilkan_produk():
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

def menu_admin():
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
            tampilkan_produk()
        elif pilih == "2":
            tambah_produk()
        elif pilih == "3":
            ubah_produk()
        elif pilih == "4":
            hapus_produk()
        elif pilih == "5":
            menu_utama()
            break
        else:
            print("Pilihan tidak valid.")
            input("Tekan Enter...")

def menu_user():
    while True:
        clear()
        print("""
=========================
|       MENU USER        |
=========================
| 1. Lihat Produk        |
| 2. Cari Produk         |
| 3. Hitung Total Harga  |
| 4. Logout              |
=========================
""")
        pilih = input("Pilih menu (1-4): ")
        if pilih == "1":
            tampilkan_produk()
        elif pilih == "2":
            nama = input("Masukkan nama produk yang ingin dicari: ")
            hasil = cari_produk(nama)
            if hasil:
                print(f"Produk ditemukan: {hasil['nama']} - Harga Rp{hasil['harga']} - Stok {hasil['stok']}")
            else:
                print("Produk tidak ditemukan.")
            input("Tekan Enter...")
        elif pilih == "3":
            try:
                nama = input("Masukkan nama produk: ")
                jumlah = int(input("Masukkan jumlah: "))
                hasil = cari_produk(nama)
                if hasil:
                    total = hitung_total(hasil['harga'], jumlah)
                    print(f"Total harga: Rp{total}")
                else:
                    raise KeyError("Produk tidak ditemukan.")
            except ValueError:
                print("Jumlah harus berupa angka.")
            except KeyError as e:
                print(e)
            finally:
                input("Tekan Enter...")
        elif pilih == "4":
            menu_utama()
            break
        else:
            print("Pilihan tidak valid.")
            input("Tekan Enter...")

def tambah_produk():
    try:
        nama = input("Nama produk: ")
        harga = int(input("Harga: "))
        stok = int(input("Stok: "))
        produk.append({"nama": nama, "harga": harga, "stok": stok})
        print("Produk berhasil ditambahkan!")
    except ValueError:
        print("Input harus berupa angka untuk harga/stok.")
    finally:
        input("Tekan Enter...")

def ubah_produk():
    tampilkan_produk()
    try:
        idx = int(input("Masukkan nomor produk yang ingin diubah: ")) - 1
        if idx < 0 or idx >= len(produk):
            raise IndexError("Nomor produk tidak valid.")
        nama = input("Nama baru: ")
        harga = input("Harga baru: ")
        stok = input("Stok baru: ")
        if nama:
            produk[idx]["nama"] = nama
        if harga.isdigit():
            produk[idx]["harga"] = int(harga)
        if stok.isdigit():
            produk[idx]["stok"] = int(stok)
        print("Produk berhasil diubah!")
    except (ValueError, IndexError) as e:
        print("Error:", e)
    finally:
        input("Tekan Enter...")

def hapus_produk():
    tampilkan_produk()
    try:
        idx = int(input("Masukkan nomor produk yang ingin dihapus: ")) - 1
        if idx < 0 or idx >= len(produk):
            raise IndexError("Nomor tidak valid.")
        del produk[idx]
        print("Produk berhasil dihapus!")
    except (ValueError, IndexError) as e:
        print(e)
    finally:
        input("Tekan Enter...")

menu_utama()