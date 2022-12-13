import datetime
nama = []
#databelanjaan = [ ["","",0,0,0] ]
databelanjaan = []
daftarbarang = [["MB001","Beras 10kg", 112900],["MB002","Beras 5kg", 56000],["MB003","Gula 1kg", 22000],["MB004","Minyak 1L", 18000],["MB005","Tepung Terigu 1kg", 18000]]

def show_data():
   
    print("Data Belanjaan")
    if(len(databelanjaan)<1):
        print("Data Kosong")
    else :
            
        for i in range(len(databelanjaan)):
            print("[",i,"]",databelanjaan[i][0]," ",databelanjaan[i][1]," ",databelanjaan[i][2]," ",databelanjaan[i][3]," ",databelanjaan[i][4])

def show_data_barang():
    print("Data Barang")
    for i in range(len(daftarbarang)):
        print("[%s] %s %d" % (daftarbarang[i][0],daftarbarang[i][1],daftarbarang[i][2] ))
      
def insert_data():
    show_data_barang()
    lagi = "Y"
    while lagi in "Y":
        kodebarang = input("Masukkan Kode Barang: ")
        kuantitas = int(input("Jumlah Qty Barang: "))
        
        #menambah ke array keranjang belanja
        for i in range(0,len(daftarbarang)):
            if(kodebarang==daftarbarang[i][0]):
                hargabarang = daftarbarang[i][2]
                totalhargabarang = kuantitas * hargabarang
            #jika ada hitung total harga buah
                #simpan data ke aray dua d  
                databelanjaan.append([kodebarang,daftarbarang[i][1],kuantitas,hargabarang,totalhargabarang])
                break
        
        lagi = input("Tambah Y/N : ")
    print()

def edit_data():
    show_data()
    indeks = int(input("Inputkan Indeks Data yang akan di edit: "))
    if(indeks > len(databelanjaan)):
        print("Indeks salah")
    else:  
        print("[",indeks,"]",databelanjaan[indeks][0]," ",databelanjaan[indeks][1]," ",databelanjaan[indeks][2]," ",databelanjaan[indeks][3]," ",databelanjaan[indeks][4])
        kuantitas_baru = int(input("Jumlah Qty Baru : "))
        databelanjaan[indeks][2] = kuantitas_baru
        harga_total_baru = kuantitas_baru * databelanjaan[indeks][3]
        databelanjaan[indeks][4] = harga_total_baru
    
def delete_data():
    show_data()
    indeks = int(input("Inputkan Indeks Data yang akan di hapus: "))
    if(indeks > len(databelanjaan)):
        print("Indeks salah")
    else:
        databelanjaan.remove(databelanjaan[indeks])

# fungsi untuk menampilkan menu
def show_menu():
    print("\n")
    print("Toko Kelontong Medan Berkah")
    if len(nama) <= 0:
        nama_baru = input("Masukkan Nama Pelanggan : ")
        nama.append(nama_baru)
    else :
        print("Pelanggan : ", nama[0])
    tanggal = datetime.datetime.now()
    print(tanggal)
    print("----------- MENU ----------")
    print("[1] Tampilkan Data Keranjang Belanja")
    print("[2] Tambah Data Belanjaan")
    print("[3] Edit Data Belanjaan")
    print("[4] Hapus Data Belanjaan")
    print("[5] Exit")
   
    menu = int(input("PILIH MENU> "))
    print()

    if menu == 1:
        show_data()
    elif menu == 2:
        insert_data()
    elif menu == 3:
        edit_data()
    elif menu == 4:
        delete_data()
    elif menu == 5:
        exit()
    else:
        print("Salah pilih!")



while(True):
    show_menu()
    