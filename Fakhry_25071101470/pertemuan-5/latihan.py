A = [[5, 3, 1],
    [2, 8, 4],
    [6, 0, 7]]

B = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

# Buatlah program python (tanpa NumPy) yang:
# a. Menjumlahkan matriks A dan B, simpan hasilnya dalam variabel C_tambah
def tambah_matriks(A, B): 
    baris, kolom = len(A), len(A[0]) 
    hasil = [[A[i][j] + B[i][j] for j in range(kolom)] for i in range(baris)] 
    return hasil

# b. Mengurangkan matriks A dikurangi B, simpan dalam variabel C_kurang
def kurang_matriks(A, B): 
    baris, kolom = len(A), len(A[0]) 
    hasil = [[A[i][j] - B[i][j] for j in range(kolom)] for i in range(baris)] 
    return hasil 

# c. Mengalikan setiap elemen matriks A dengan skalar k = 4 , simpan dalam C_skalar
def kali_skalar(matriks, k): 
    hasil = [] 
    for baris in matriks: 
        baris_baru = [elemen * k for elemen in baris] 
        hasil.append(baris_baru) 
    return hasil 

# d. Menampilkan ketiga hasil dengan format rapi baris per baris
print('Soal a')
C_tambah = tambah_matriks(A, B) 
for baris in C_tambah: 
    print(baris)

print('')
print('Soal b')
C_kurang = kurang_matriks(A, B) 
for baris in C_kurang: 
    print(baris)

print('')
print('Soal c')
C_skalar = kali_skalar(A, 4) 
for baris in C_skalar: 
    print(baris) 