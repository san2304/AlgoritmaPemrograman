#open file
data = open("data_iris.txt","r")
print ("Nama File",data.name)

#read
file_konten = data.read(100)
print ("Isi Data :",file_konten[17:38])

#closed
data.close()