inputLagi = "Y"
daftarSiswa = []

while inputLagi in "Y" :
    nama = input("Masukkan Nama kamu : ")
    tanggal_lahir = input("Masukkan Tanggal Lahir kamu : ")

    daftarSiswa.append([nama,tanggal_lahir])
                       
    inputLagi = input("Input lagi Y/N?")

print(daftarSiswa)