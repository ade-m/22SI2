
def hitung_faktorial(n):
    if (n > 2) :
        return n * hitung_faktorial(n-1)
    return n

hasil = hitung_faktorial(5)
print(hasil)