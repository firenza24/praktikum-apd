from prettytable import PrettyTable
from data import produk, clear
from akun import login, registrasi
from hitung import hitung_total


def tampilkan_produk():
    clear()
    print("============= DAFTAR PRODUK =============")
    if not produk:
        print("Belum ada produk.")
    else:
        tabel = PrettyTable()
        tabel.field_names = ["No", "Nama Produk", "Harga (Rp)", "Stok"]
        for i, p in enumerate(produk, start=1):
            tabel.add_row([i, p["nama"], f"Rp{p['harga']:,}", p["stok"]])
        print(tabel)
    input("\nTekan Enter untuk kembali...")


def cari_produk(nama_produk):
    for p in produk:
        if p["nama"].lower() == nama_produk.lower():
            return p
    return None


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
        input("Tekan Enter untuk lanjut...")


def ubah_produk():
    tampilkan_produk()
    try:
        idx = int(input("Masukkan nomor produk yang ingin diubah: ")) - 1
        if idx < 0 or idx >= len(produk):
            raise IndexError("Nomor produk tidak valid.")
        nama = input("Nama baru (kosongkan jika tidak diubah): ")
        harga = input("Harga baru (kosongkan jika tidak diubah): ")
        stok = input("Stok baru (kosongkan jika tidak diubah): ")

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
        input("Tekan Enter untuk lanjut...")


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
        input("Tekan Enter untuk lanjut...")


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
            print("Logout berhasil.")
            input("Tekan Enter...")
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
            nama = input("Masukkan nama produk: ")
            hasil = cari_produk(nama)
            if hasil:
                print(f"{hasil['nama']} - Rp{hasil['harga']:,} - Stok {hasil['stok']}")
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
                    print(f"Total harga: Rp{total:,}")
                else:
                    print("Produk tidak ditemukan.")
            except ValueError:
                print("Jumlah harus angka.")
            input("Tekan Enter...")
        elif pilih == "4":
            print("Logout berhasil.")
            input("Tekan Enter...")
            menu_utama()
            break
        else:
            print("Pilihan tidak valid.")
            input("Tekan Enter...")


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
    pilih = input("Pilih menu (1-3): ")
    if pilih == "1":
        login()
    elif pilih == "2":
        registrasi()
    elif pilih == "3":
        print("Terima kasih telah menggunakan program ini.")
        exit()
    else:
        print("Pilihan tidak valid.")
        input("Tekan Enter...")
        menu_utama()
