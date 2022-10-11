#deklarasi 
N=2
namaBarang=""
kodeBarang=""
hargaBarang=0
jenisBarang=""
diskon=0.0

#program
#for 1 to N
for i in range(1,N+1) :
    kodeBarang= input("Kode Barang \t:\t")
    namaBarang= input("Nama Barang \t:\t")
    hargaBarang= input("Harga Barang \t:\t")
    jenisBarang= input("Jenis Barang \t:\t")
    #cek Diskon
    #atk if (false or true or false) => true +-/*^
    if (jenisBarang in "ATK") or (jenisBarang in "atk") or (jenisBarang in "Atk"):
        diskon=0.02
    elif jenisBarang in "Snack" or jenisBarang in "snack" :
        diskon=0.05
    elif jenisBarang in "Sembako" or jenisBarang in "sembako" :
        diskon=0.15
    else :
        diskon=0.0
    print("Diskon \t\t:\t",diskon)
