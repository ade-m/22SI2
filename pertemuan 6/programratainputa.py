#deklarasi
N = int(input("input N :"))
masukan=0
total =0

for i in range(N):
    masukan = int(input("input Sebuah Nilai :"))
    total += masukan

print("Total Nilai : ", total)
print("Rata-R=rata Nilai : ", total/N)