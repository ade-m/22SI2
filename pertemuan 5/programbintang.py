#deklarasi
n=int(input("Masukkan N: "))
#mode = int(input("Masukkan Mode (1. bintang, 2.Angka): "))

i=1

for i in range(1,n+1) :
    j=1
   
    for j in range(1,i+1) :
        print(j,end="")
    print("")

i=1

for i in range(n,0,-1) :
    j=1
   
    for j in range(1,i+1) :
        print(j,end="")
    print("")
   # for j in range(1,i+1) :
 #   if(mode==1):
  #      print("*",end="")
   # else :    
    #    print(j,end="")
print("")