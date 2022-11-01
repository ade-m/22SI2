inputLagi = "Y"
daftarKaryawan = []

while inputLagi in "Y" :
    nama = input("Masukkan Nama  : ")
    gaji = int(input("Masukkan Gaji dalam $ : "))

    daftarKaryawan.append([nama,gaji])
                       
    inputLagi = input("Input lagi Y/N?")

jlhGaji =0
for i in range(len(daftarKaryawan)):
    print(daftarKaryawan[i][0], end="\t")
    print(daftarKaryawan[i][1])
    jlhGaji +=daftarKaryawan[i][1]

print("total gaji ",jlhGaji)
    