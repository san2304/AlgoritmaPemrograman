#setting variabel identitas 
nim   = int(input("Masukan NIM     : "))
nama  = input("Masukan Nama    : ")
kelas = int(input("Masukan Kelas   : "))
prodi = input("Masukan Jurusan : ")

name = input("Maukan Nama Bangunan : ")
r = int(input("Jari-Jari : "))
phi = 3.14

#opeasi
luas = phi*r*r

#tapilan A
print ("A")
print ("================================")
print ("      OPERASI ARITMAITKA        ")
print ("================================")
print ("")
print ("Nim anda          :%d"%(nim))
print ("Nama lengkap anda :%s"%(nama))
print ("Kelas anda        :%d"%(kelas))
print ("Progam Studi anda :%s"%(prodi))
print ("")
print ("--------------------------------")
print ("   Bangunan %s"%(nama))
print ("--------------------------------")
print ("")
print ("Nilai Jari-Jari :%d"%(r))
print ("Luas Bangunan   :%d"%(luas))
print ("")
print ("================================")

#list
san= ["UNISS","di","belajar","pada","Mahasiswa","Pemrograan","ruang","lab","Algoritma","semester","topik","Data","Tipe","dan","dengan","Batang",2]
#       0      1      2        3        4           5           6     7      8            9          10    11     12     13     14       15    16

#tapilan B
print ("B")
print ("=====================================================================================================")
print ("                                  SUSUN KATA SPOK         ")
print ("=====================================================================================================")
print ("")
print (san[4],san[0],san[15],san[9],san[16],san[2],san[8],san[13],san[5],san[14],san[10],san[12],san[11],san[1],san[6],san[7])
print ("")
print ("=====================================================================================================")