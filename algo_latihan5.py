tuple_1 = ("Faqih", "Nicko", "Ageng", "Ikhsan", "Adin")
tuple_2 = ("23", "42", "12", "53", "64")
tuple_3 = ("Puri", "Putri", "Syifa", "Anggun")

print(tuple_1)
print(tuple_2)
print(tuple_3)

# Membuat tuple yang kosong
empty_tuple = ()
print("Tuple kosong:", empty_tuple)

# Tuple dengan kombinasi tipe data
int_tuple = (4, 6, 8, 10, 12, 14)
print("Tuple bernilai integer:", int_tuple)

# Tuple dengan kombinasi tipe data
mixed_tuple = (4, "Python", 9.3)
print("Tuple dengan tipe data yang berbeda:", mixed_tuple)

# Tuple bersarang
nested_tuple = ("Python", {4: 5, 6: 2, 8: 2}, (5, 3, 5, 6))
print("Tuple bersarang:", nested_tuple)

print()
print()
print()

identitas = ("Ikhsan", 27, "Indonesia")
prodi_1 = ("Informatika", 10)
prodi_2 = ("Sistem Informasi", 11)
dosen_1 = (10, "Mr Mbahmboh")
dosen_2 = (11, "Mrs SaanNane")

print("------------------------------")
print("Cetak Semua Data")
print("------------------------------")
print("Nama: %s, Usia: %d, Negara: %s" % (identitas[0], identitas[1], identitas[2]))
print("------------------------------")
print("Cek Program Studi")
print("------------------------------")
print("Program Studi 1:\nNama Prodi Pertama: %s, ID: %d" % (prodi_1[0], prodi_1[1]))
print("------------------------------")
print("Dosen Pengampu")
print("------------------------------")
print("Dosen Informatika: %s, ID: %d" % (dosen_1[1], dosen_1[0]))
print("Dosen Sistem Informasi: %s, ID: %d" % (dosen_2[1], dosen_2[0]))
print(type(identitas), type(prodi_1), type(prodi_2), type(dosen_1), type(dosen_2))

print()
print()
print()

my_list = [1, 2, 3, 4, 5]

# Forward
print("------------------------------")
print("forward")
print("------------------------------")
print(my_list[1])
print(my_list[3:])
print(my_list[:1])
print(my_list[1])
print(my_list[1:3])

# Backward
print("------------------------------")
print("backward")
print("------------------------------")
print(my_list[-1])
print(my_list[-3:])
print(my_list[:-1])
print(my_list[-2])
print(my_list[-1:-3:-1])
