def linearSearch(arr, targetVal):
    for i in range(len(arr)):
        if arr[i] == targetVal:
            return i
    return -1

def binarySearch(arr, targetVal):
    arr = sorted(arr)
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == targetVal:
            return mid

        if arr[mid] < targetVal:
            left = mid + 1
        else:
            right = mid - 1

    return -1

data = [59, 40, 36, 40, 30, 26, 97, 8, 23, 31, 2, 40, 99, 70, 64, 36, 43, 20, 1, 9]

Pencarian = int(input('Masukkan Data Yang dicari: '))\

# LINEAR SEARCH
result = linearSearch(data, Pencarian)
if result != -1:
    print("Linear Search: Ditemukan Di Indeks", result)
else:
    print("Linear Search: Tidak Ditemukan")

# BINARY SEARCH
result1 = binarySearch(data, Pencarian)
if result1 != -1:
    print("Binary Search: Ditemukan Di Indeks", result1)
else:
    print("Binary Search: Tidak Ditemukan")