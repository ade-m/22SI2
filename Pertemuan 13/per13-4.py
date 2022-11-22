def faktorial(x):
    fX=1
    for i in range (1,x+1):
        fX *=i
    return fX

# Main Program
x = int(input("Masukkan nilai x : "))

nilai_faktorial = faktorial(x)

print("Nilai Faktorial ", x, " adalah ", nilai_faktorial)