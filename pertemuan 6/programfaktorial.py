#deklarsi
x = int(input("Masukkan nilai x : "))
fX=1
for i in range (1,x+1):
    fX *=i

print("Nilai Faktorial ", x, " adalah ", fX)