#Deklarasi
nama_pelanggan =""
status_member = "tidak"
total_belanja = 0
diskon_persen ="0%"
diskon_idr = 0
total_bayar = 0

inputlagi = "Y"
#program
while inputlagi in "Y" :
    #input
    inputlagi ="n"
    nama_pelanggan = input("Nama Pelanggan : ")
    status_member = input("Status Member (Ya/Tidak) : ")
    total_belanja = int(input("Total Belanjaan (IDR) : "))

    #cek status member
    if status_member in "Ya" :
        #cek total belanjaan dan hitung diskon
        if total_belanja < 100000 :
            diskon_persen = "1%"
            diskon_idr = int((1/100)*total_belanja)
        elif  total_belanja < 1000000 :
            diskon_persen = "5%"
            diskon_idr = int((5/100)*total_belanja)
        elif  total_belanja > 1000000 :
            diskon_persen = "10%"
            diskon_idr = int((10/100)*total_belanja)
            if diskon_idr >100000 :
                diskon_idr = 100000
        else :
            diskon_idr =0
            diskon_persen = "0%"
    elif status_member in "Tidak" :
        #cek total belanjaan dan hitung diskon
        if total_belanja < 100000 :
            diskon_persen = "0%"
            diskon_idr = int((0/100)*total_belanja)
        elif  total_belanja < 1000000 :
            diskon_persen = "1%"
            diskon_idr = int((1/100)*total_belanja)
        elif  total_belanja > 1000000 :
            diskon_persen = "3%"
            diskon_idr = int((3/100)*total_belanja)
            if diskon_idr >100000 :
                diskon_idr = 100000
        else :
            diskon_idr =0
            diskon_persen = "0%"

    total_bayar = total_belanja - diskon_idr

    #cetak / tampilkan output
    print("Diskon % : ", diskon_persen)
    print("Diskon (IDR) : ",diskon_idr)
    print("Total Bayar (IDR) : ", total_bayar)

    inputlagi = input("Input Lagi (Y/T) : ")
