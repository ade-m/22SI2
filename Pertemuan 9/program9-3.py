
inputLagi = "Y"
daftarBuah = []

while inputLagi in "Y" :
    inputLagi = "N"
    buah = input("Masukkan Buah kesukaan kamu : ")
    daftarBuah.append(buah)
    inputLagi = input("Tambah buah lagi Y/N?")

print(daftarBuah)
