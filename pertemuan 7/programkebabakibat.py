#deklarasi
daging = 5000
tkecil=0
tbesar=0

while daging>0:
    pesanan = input("Jenis Kebab (Besar/Kecil)")
    qty = int(input("Jumlah : "))
    if(pesanan in "Besar"):
        daging = daging - (200*qty)
        tbesar+=qty
    else :
        daging = daging - (100*qty)
        tkecil +=qty
    print("Sisa Daging : ",daging," gr")
print("Kebab Kecil : ",tkecil," pcs")
print("Kebab Besar : ",tbesar," pcs")
print("Kebab Terjual : ",(tbesar+tkecil)," pcs")