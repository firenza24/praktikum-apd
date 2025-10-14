import os

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

produk = [
    ["Sofa", 75000, 10],
    ["Lampu Tidur", 125000, 5],
    ["Gantungan Kunci", 15000, 20]
]

user = [["rega", "123", "admin"]]

def tampilkan_produk():
    print("\n=========== DAFTAR PRODUK ===========")
    if len(produk) == 0:
        print("Belum ada produk.")
    else:
        print("No | Nama Produk       | Harga  | Stok")
        print("--------------------------------------")
        for i in range(len(produk)):
            print(f"{i+1}.  {produk[i][0]:17} {produk[i][1]:8}   {produk[i][2]}")

def tambah_produk():
    clear()
    print("=== TAMBAH PRODUK ===")
    nama = input("Nama produk: ")
    harga = input("Harga: ")
    stok = input("Stok: ")

    if nama != "" and harga.isdigit() and stok.isdigit():
        produk.append([nama, int(harga), int(stok)])
        print("Produk berhasil ditambahkan!")
    else:
        print("Input tidak valid.")
    input("\nTekan Enter untuk kembali...")

def ubah_produk():
    clear()
    tampilkan_produk()
    print("\n=== UBAH PRODUK ===")
    pilih = input("Masukkan nomor produk: ")
    if pilih.isdigit():
        idx = int(pilih)-1
        if 0 <= idx < len(produk):
            nama = input("Nama baru (kosongkan jika tidak diubah): ")
            harga = input("Harga baru (kosongkan jika tidak diubah): ")
            stok = input("Stok baru (kosongkan jika tidak diubah): ")

            if nama != "":
                produk[idx][0] = nama
            if harga.isdigit():
                produk[idx][1] = int(harga)
            if stok.isdigit():
                produk[idx][2] = int(stok)
            print("Produk berhasil diubah!")
        else:
            print("Nomor tidak ditemukan.")
    else:
        print("Input tidak valid.")
    input("\nTekan Enter untuk kembali...")

def hapus_produk():
    clear()
    tampilkan_produk()
    print("\n=== HAPUS PRODUK ===")
    pilih = input("Masukkan nomor produk: ")
    if pilih.isdigit():
        idx = int(pilih)-1
        if 0 <= idx < len(produk):
            produk.pop(idx)
            print("Produk berhasil dihapus!")
        else:
            print("Nomor tidak ditemukan.")
    else:
        print("Input tidak valid.")
    input("\nTekan Enter untuk kembali...")

def menu_admin():
    while True:
        clear()
        print("=== MENU ADMIN ===")
        print("1. Lihat Produk")
        print("2. Tambah Produk")
        print("3. Ubah Produk")
        print("4. Hapus Produk")
        print("5. Logout")
        pilih = input("Pilih: ")

        if pilih == "1":
            clear()
            tampilkan_produk()
            input("\nTekan Enter...")
        elif pilih == "2":
            tambah_produk()
        elif pilih == "3":
            ubah_produk()
        elif pilih == "4":
            hapus_produk()
        elif pilih == "5":
            break
        else:
            print("Pilihan tidak valid.")
            input("Tekan Enter...")

def menu_user(nama):
    while True:
        clear()
        print(f"=== MENU USER ({nama}) ===")
        print("1. Lihat Produk")
        print("2. Logout")
        pilih = input("Pilih: ")

        if pilih == "1":
            clear()
            tampilkan_produk()
            input("\nTekan Enter...")
        elif pilih == "2":
            break
        else:
            print("Pilihan tidak valid.")
            input("Tekan Enter...")

def register():
    clear()
    print("=== REGISTER ===")
    uname = input("Username baru: ")
    pw = input("Password: ")

    if uname != "" and pw != "":

        ada = False
        for u in user:
            if u[0] == uname:
                ada = True
        if ada:
            print("Username sudah terdaftar!")
        else:
            user.append([uname, pw, "user"])
            print("Registrasi berhasil!")
    else:
        print("Input tidak boleh kosong.")
    input("\nTekan Enter untuk kembali...")

def login():
    clear()
    print("=== LOGIN ===")
    uname = input("Username: ")
    pw = input("Password: ")

    for u in user:
        if u[0] == uname and u[1] == pw:
            print(f"Selamat datang, {uname}!")
            input("Tekan Enter...")
            if u[2] == "admin":
                menu_admin()
            else:
                menu_user(uname)
            return
    print("Username atau password salah!")
    input("\nTekan Enter...")

def main():
    while True:
        clear()
        print("=== TOKO AKSESORIS RUMAH ===")
        print("1. Login")
        print("2. Register")
        print("3. Keluar")
        pilih = input("Pilih: ")

        if pilih == "1":
            login()
        elif pilih == "2":
            register()
        elif pilih == "3":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid.")
            input("Tekan Enter...")

main()