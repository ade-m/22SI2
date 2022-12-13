def hitung_pangkat(bilangan,pangkat):
    if(pangkat>1):
        return bilangan * hitung_pangkat(bilangan,pangkat -1)
    
    return bilangan

hasil = hitung_pangkat(10,4)
print(hasil)