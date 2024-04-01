# akun = str(input("Masukkan Nama atau NIM : "))
# terdaftar = ['Rafli Miftahul Bachtiar', '23090117']
# if akun not in terdaftar:
#     print("Daftarkan akun anda terlebih dahulu")
#     str(input("Masukkan Nama : "))
#     str(input("Masukkan NIM : "))

judul_buku = str(input("Masukkan judul buku : "))
pengarang = str(input("Masukkan nama pengarang : "))
tahun_terbit = str(input("Masukkan tahun terbit : "))

print([f"Judul : " + judul_buku])
print([f"Pengarang : " + pengarang])
print([f"Tahun terbit : " + tahun_terbit])

buku = ["Dilan, Dia adalah dilanku tahun 1990", "Pidi Baiq", "2018", "Rak [12]"]

if judul_buku and pengarang and tahun_terbit in buku:
    print(f"Silahkan Ambil Buku di " + buku[3])
else:
    print("Anda salah memasukkan data")