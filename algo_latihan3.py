#setting variabel identitas 

nim   = input("Masukan NIM     : ")

nama  = input("Masukan Nama    : ")

kelas = input("Masukan Kelas   : ")

prodi = input("Masukan Jurusan : ")

#settung variabel nilai

bhs_ind = int(input("Nilai Bahasa Indonesia : "))

bhs_ing = int(input("Nilai Bahasa Inggris   : "))

pd      = int(input("Nilai Pemrograman Dasar     : "))

mtk     = int(input("Nilai Matematika   : "))

kal1    = int(input("Nilai Kalkulus 1    : "))

os      = int(input("Nilai Sistem Operasi   : "))

#perhitungan

rata = (bhs_ind+bhs_ing+pd+mtk+kal1+os)/6

#grade nilai

if 0 < bhs_ind <= 60:

    grade_ind = "C"

elif 60 < bhs_ind <= 75:

    grade_ind = "B"

elif 75 < bhs_ind <= 85:

    grade_ind = "AB"

elif 85 < bhs_ind <= 100:

    grade_ind = "A"

else:

    grade_ind = "Grade Anda Tidak ditemukan!"

if 0 < bhs_ing <= 60:

    grade_ing = "C"

elif 60 < bhs_ing <= 75:

    grade_ing = "B"

elif 75 < bhs_ing <= 85:

    grade_ing = "AB"

elif 85 < bhs_ing <= 100:

    grade_ing = "A"

else:

    grade_ing = "Grade Anda Tidak ditemukan!"

if 0 < pd <= 60:

    grade_pd = "C"

elif 60 < pd <= 75:

    grade_pd = "B"

elif 75 < pd <= 85:

    grade_pd = "AB"

elif 85 < pd <= 100:

    grade_pd = "A"

else:

    grade_pd = "Grade Anda Tidak ditemukan!"

if 0 < mtk <= 60:

    grade_mtk = "C"

elif 60 < mtk <= 75:

    grade_mtk = "B"

elif 75 < mtk <= 85:

    grade_mtk = "AB"

elif 85 < mtk <= 100:

    grade_mtk = "A"

else:

    grade_mtk = "Grade Anda Tidak ditemukan!"

if 0 < kal1 <= 60:

    grade_kal1 = "C"

elif 60 < kal1 <= 75:

    grade_kal1 = "B"

elif 75 < kal1 <= 85:

    grade_kal1 = "AB"

elif 85 < kal1 <= 100:

    grade_kal1 = "A"

else:

    grade_kal1 = "Grade Anda Tidak ditemukan!"

if 0 < os <= 60:

    grade_os = "C"

elif 60 < os <= 75:

    grade_os = "B"

elif 75 < os <= 85:

    grade_os = "AB"

elif 85 < os <= 100:

    grade_os = "A"

else:

    grade_mtk = "Grade Anda Tidak ditemukan!"

#grade rata

if (rata > 0 and rata <= 60):

  grade_rata = ("C")

elif (rata > 60 and rata <= 75):

  grade_rata = ("B")

elif (rata > 75 and rata <= 85):

  grade_rata = ("AB")

elif (rata > 85 and rata <= 100):

  grade_rata = ("A")

else:

  grade_rata = (" Grade Anda Tidak ditemukan!")

#menampilkan

print ("-------------------------------------")

print ("    Kartu Hasil Studi     ")

print ("  Uniss Kampus 2 Batang   ")

print ("-------------------------------------")

print ("")

print ("Nim anda          : ",nim)

print ("Nama lengkap anda : ",nama)

print ("Kelas anda        :",kelas)

print ("Progam Studi anda :",prodi)

print ("")

print ("-------------------------------------")

print ("No   Mata Kuliah      Nilai  Grade")

print ("-------------------------------------")

print ("")

print ("1. Bahasa Indonesia  =",bhs_ind,"   ",grade_ind)

print ("2. Bahasa Inggris    =",bhs_ing,"   ",grade_ing)

print ("3. Pemrograman Dasar =",pd,"   ",grade_pd)

print ("4. Matematika        =",mtk,"   ",grade_mtk)

print ("5. Kalkulus 1        =",kal1,"   ",grade_kal1)

print ("6. Sistem Operasi    =",os,"   ",grade_os)

print ("")

print ("-------------------------------------")

print ("")

print ("Rata-Rata",rata,"               ",grade_rata)

print ("")

print ("-------------------------------------")
