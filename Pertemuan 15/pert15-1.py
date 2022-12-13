def halo_dunia():
    print("Halo Dunia")
    #panggil diri sendiri
    halo_dunia()
    
#halo_dunia()


# for i in range(10):
#     print(i)

def tampilAngka(batas, i=0):
    print(i)
    
    if(i<batas):
        #disinilah fungsi rekursifitas di panggil
        tampilAngka(batas,i+1)


tampilAngka(10)

