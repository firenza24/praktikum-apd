from data import pengguna, clear

def registrasi():
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


def login():
    from menu import menu_admin, menu_user, menu_utama
    clear()
    print("=== LOGIN ===")
    uname = input("Username: ")
    pw = input("Password: ")

    for p in pengguna:
        if p["username"] == uname and p["password"] == pw:
            print(f"Selamat datang, {uname}!")
            input("Tekan Enter...")
            if p["role"] == "admin":
                menu_admin()
            else:
                menu_user()
            return

    print("Login gagal! Username atau password salah.")
    input("Tekan Enter...")
    menu_utama()