def ganjil_genap(bilangan):
    if(bilangan % 2 ==0):
        return True
    else:
        return False

angka = int(input("Masukkan Angka : "))

if(ganjil_genap(angka)):
    print("Bilangan ", angka, " adalah genap")
else:
    print("Bilangan ", angka, " adalah ganjil")


    