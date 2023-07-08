data = input("Tambah data : ")

# Membuka file dalam mode tambah (append) dan membaca (read)
file = open("data_iris.txt", "a+")

# Memindahkan posisi penulis ke akhir file
file.seek(0, 2)

# Menambahkan data ke dalam file
file.write(data)

# Menutup file
file.close()