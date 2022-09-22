#input
diskon = 0
namapelanggan = input("Masukkan Nama Pelanggan ")
pesanan = input("Masukkan Nama Pesanan ")
totalbelanja = int(input("Masukkan Total Bayar "))

#percabangan
if "agus" in namapelanggan or "Agus" in namapelanggan :
    if "kopi tubruk" in pesanan :
        diskon = int((70/100)*totalbelanja)
        print("Diskon : Agus 70%")
    elif "roti sobek" in pesanan :
        diskon = int((40/100)*totalbelanja)
        print("Diskon : Agus 40%")
    else :
        diskon = 0
        
    
totalbayar = totalbelanja - diskon
print("Diskon (IDR) : ",diskon)
print("Total Bayar (IDR) : ",totalbayar)
 