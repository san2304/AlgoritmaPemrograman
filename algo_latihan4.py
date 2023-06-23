#jumlah barang
sarimi = 5#int(input("Jumlah sarimi : "))
ndok   = 5#int(input("Jumlah ndok   : "))
micin  = 5#int(input("Jumlah micin  : "))
lenga  = 5#int(input("Jumlah lenga  : "))
lombok = 5#int(input("Jumlah lombok : "))
beras  = 5#int(input("Jumlah beras  : "))

#jumlahe
j_sarimi = 2500*sarimi
j_ndok = 2000*ndok
j_micin = 1000*micin
j_lenga = 15000*lenga
j_lombok = 5000*lombok
j_beras = 9000*beras

#belonjone
belonjo = (j_sarimi+j_ndok+j_micin+j_lenga+j_lombok+j_beras)

#diskontol
if belonjo > 200000:
  diskon = belonjo*0.2
else:
  diskon = 0 
f_diskon = f"{diskon:.2f}".rstrip("0").rstrip(".")

#total rego
rego = belonjo-diskon
f_rego = f"{rego:.2f}".rstrip("0").rstrip(".")

#tampilane
print ("        BERKAH_MA'E/03/(081)2345678     ")
print ("")
print ("---------------------------------------------")
import datetime
waktu = datetime.datetime.now()
f_waktu = waktu.strftime("%Y-%m-%d %H:%M")
print(f_waktu,"               12042/SANN/02")
print ("---------------------------------------------")
print ("")
print ("No | NamaProduk  | Qty |  Harga   | Jumlah ")
print ("")
print ("1. Sarimi         ",sarimi,"   Rp 2.500 ","","Rp",j_sarimi)
print ("2. Ndok           ",ndok,"   Rp 2.000 ","","Rp",j_ndok)
print ("3. Micin          ",micin,"   Rp 1.000"," ","Rp",j_micin)
print ("4. Lenga          ",lenga,"   Rp 15.000","","Rp",j_lenga)
print ("5. Lombok         ",lombok,"   Rp 5.000"," ","Rp",j_lombok)
print ("6. Beras          ",beras,"   Rp 9.000"," ","Rp",j_beras)
print ("                   --------------------------")
print ("                   Total Belanja : Rp",belonjo)
print ("                   Diskon        : Rp",f_diskon)
print ("                   --------------------------",)
print ("")
print ("                   Total Harga   : Rp",f_rego)

#bayar
bayar = int(input("                   Bayar         : Rp "))
while bayar < rego:
    print("Duet mu kurang su'")
    bayar = int(input("                   Bayar Ulang   : Rp "))
  
#kembali
sosok = bayar-rego
f_sosok = f"{sosok:.2f}".rstrip("0").rstrip(".")

print ("                   Kembalian     : Rp",f_sosok)
print ("")
print ("")
print ("")
print ("             Suwon Wes Belonjo Bolo' ")
