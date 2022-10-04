#deklarasi
A = 11
i = 2
isbilanganPrima = True

for i in range (2,A) :
    if A%i==0 :
        isbilanganPrima=False
        break
    else :
        isbilanganPrima=True

if isbilanganPrima :
    print(A, " adalah bilangan Prima")
else:
    print(A, " bukan bilangan Prima")