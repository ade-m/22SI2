#deklarasi 

A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[9,8,7],[6,5,4],[3,2,1]]
C = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            C[i][j] +=A[i][k] * B[k][j]

#cetak C
#perulangan utk baris
for i in range(0,len(C)):
    #perulangan utk kolom
    for j in range(0,len(C[0])):
        print(C[i][j], end="\t")
    print()