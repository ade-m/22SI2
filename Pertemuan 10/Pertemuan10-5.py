#deklarasi 

A = [[1,2],[4,5]]
B = [[9,8],[6,5]]
C = [[0,0],[0,0]]

for i in range(0,2):
    for j in range(0,2):
        for k in range(0,2):
            C[i][j] +=A[i][k] * B[k][j]

#cetak C
#perulangan utk baris
for i in range(0,len(C)):
    #perulangan utk kolom
    for j in range(0,len(C[0])):
        print(C[i][j], end="\t")
    print()