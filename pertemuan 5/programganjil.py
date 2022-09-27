#deklarasi
import genericpath


n=10
i=0

#program perulangan for
for i in range(n,0,-1):

    if i ==5:
        pass
    if i % 2 != 0 :
        print(i, ": Bilangan ganjil")
    else :
        print(i,": Bilangan Genap")

#program perulangan while
i= 30
while i>0 :
    if i==10:
        break
    if i % 2 != 0 :
        print(i, ": Bilangan ganjil")
    else :
        print(i,": Bilangan Genap")
    i-=1

# n =6

#       1
##      12
###     123
####    1234
#####   12345
######  123456

# n=3

#     1
##    12
###   123