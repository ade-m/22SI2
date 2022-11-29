nama = []


#Fungsi Tampil Menu
def show_menu():
    print()
    print("----------Menu----------")
    print("[1] Show Data")
    print("[2] Insert Data")
    print("[3] Edit Data")
    print("[4] Delete Data")
    print("[5] Exit")
    
    menu = int(input("Pilih Menu > "))
    print()
    
    if menu == 1 :
        show_data()
    elif menu == 2:
        insert_data()
    elif menu == 3:
        edit_data()
    elif menu == 5:
        exit()

#Fungsi Tampil Data
def show_data():
    if len(nama)<=0:
        print("Data masih kosong")
    else:
        for i in range(len(nama)):
            print("[%d] %s" % (i, nama[i]))

def insert_data():
    nama_baru = input("Masukkan Nama anda :")
    nama.append(nama_baru)
            
def edit_data():
    show_data()
    indeks = int(input("Masukkan Indeks Data : "))
    if indeks > len(nama):
        print("Input Salah")
    else:
        nama_baru = input("Masukkan Nama baru :")
        nama[indeks] = nama_baru
    
#Program Utama
jalan = True
while(jalan):
    show_menu()
            

                  
               