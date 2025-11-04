import os
from prettytable import PrettyTable

produk = [
    {"nama": "Sofa", "harga": 75000, "stok": 10},
    {"nama": "Lampu Tidur", "harga": 125000, "stok": 5},
    {"nama": "Gantungan Kunci", "harga": 15000, "stok": 20}
]

pengguna = [
    {"username": "rega", "password": "123", "role": "admin"}
]

login_user = None

# ✅ Tambahkan fungsi clear() di sini
def clear():
    os.system("cls" if os.name == "nt" else "clear")


def tampilkan_produk():
    clear()
    print("============= DAFTAR PRODUK =============")

    if not produk:
        print("Belum ada produk.")
    else:
        tabel = PrettyTable()
        tabel.field_names = ["No", "Nama Produk", "Harga (Rp)", "Stok"]
        for i, p in enumerate(produk, start=1):
            tabel.add_row([i, p["nama"], p["harga"], p["stok"]])
        print(tabel)
    input("\nTekan Enter untuk kembali...")


def cari_produk(nama_produk):
    for p in produk:
        if p["nama"].lower() == nama_produk.lower():
            return p
    return None