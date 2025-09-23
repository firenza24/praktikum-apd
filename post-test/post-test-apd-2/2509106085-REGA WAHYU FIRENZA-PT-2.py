nama = input ("Masukkan nama lengkap:")
NIM = input("Masukkan NIM:")
harga = float(input("Masukkan harga menu makanan:"))

pajak_lele = harga * 0.05
total_lele = harga + pajak_lele

pajak_mie = harga * 0.08
total_mie = harga + pajak_mie

pajak_padang = harga * 0.10
total_padang = harga + pajak_padang

print(f"{nama} dengan NIM {NIM} ingin membeli makanan seharga Rp {harga:.2f}")

print(f"jika membeli pecel lele , maka harus membayar Rp {total_lele:.2f} setelah mendapat pajak 5%")
print(f"jika membeli mie ayam , maka harus membayar Rp {total_mie:.2f} setelah mendapat pajak 8%")
print(f"jika membeli nasi padang , maka harus membayar Rp {total_padang:.2f} setelah mendapat pajak 10%")