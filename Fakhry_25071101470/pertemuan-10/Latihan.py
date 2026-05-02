# Buatlah sebuah program Python yang berjalan di terminal dengan ketentuan sebagai berikut:

# Program meminta pengguna untuk memasukkan jumlah elemen yang akan dimasukkan ke dalam array.
# Selanjutnya, pengguna memasukkan sejumlah bilangan bulat non-negatif sesuai jumlah yang telah ditentukan, satu per satu.
# Setelah semua elemen dimasukkan, program akan mengurutkan array tersebut menggunakan dua algoritma pengurutan, yaitu Radix Sort dan Merge Sort, secara terpisah.
# Program menampilkan hasil pengurutan dari masing-masing algoritma ke layar terminal.
# Input yang diterima hanya bilangan bulat non-negatif (≥ 0). Program harus menangani input yang tidak valid.
# Implementasikan fungsi terpisah untuk Radix Sort dan Merge Sort.
# Tampilkan array sebelum dan sesudah diurutkan untuk setiap algoritma.

array = []
n = int(input('Masukkan Jumlah Elemen: '))

for i in range(n):
    n1 = int(input(f'Masukkan bilangan ke-{i+1}: '))
    if n1 < 0:
        print('Input Tidak Valid!')
    else:
        array.append(n1)

def radixSort(array):
    radixArray = [[],[],[],[],[],[],[],[],[],[]]
    maxVal = max(array)
    exp = 1

    while maxVal // exp > 0:
        while len(array) > 0:
            val = array.pop()
            radixIndex = (val // exp) % 10
            radixArray[radixIndex].append(val)

        for bucket in radixArray:
            while len(bucket) > 0:
                val = bucket.pop()
                array.append(val)

        exp *= 10
    return array

def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]

    sortedLeft = mergeSort(leftHalf)
    sortedRight = mergeSort(rightHalf)

    return merge(sortedLeft, sortedRight)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

print(f'array awal: {array}')
print(f'RadixSort: {radixSort(array)}')
print(f'MergeSort: {mergeSort(array)}')