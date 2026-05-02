python_data = [ 918, 336, 637, 814, 507, 685, 854, 933, 970, 461, 26, 884, 684, 47, 922, 246, 431, 985, 412, 679, 708, 354, 
               369, 396, 406, 882, 119, 682, 378, 578, 208, 899, 344, 436, 153, 835, 836, 985, 117, 619, 225, 345, 210, 606, 
               313, 998, 681, 989, 212, 163, 762, 389, 906, 423, 204, 627, 430, 568, 430, 71, 429, 492, 817, 577, 621, 914, 
               500, 783, 872, 992, 498, 477, 34, 570, 113, 2, 58, 844, 464, 293, 302, 183, 711, 777, 71, 441, 261, 713, 544,
               528, 759, 193, 163, 272, 389, 979, 608, 977, 721, 508, 619, 875, 948, 750, 991, 711, 855, 111, 555, 608, 535, 
               603, 538, 753, 190, 441, 85, 200, 193, 577, 774, 578, 405, 306, 256, 926, 433, 444, 459, 368, 187, 671, 701, 
               714, 411, 940, 603, 736, 665, 947, 517, 19, 365, 165, 514, 133, 491, 642, 636, 957]

def bubble_sort(data):
    n = len(data)
    swapped = False
    swap = 0
    for i in range(n-1):
        for j in range(n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                swapped = True
                swap += 1
            if not swapped:
                break
    return data, swap


def select_sort(data):
    n = len(data)
    swap1 = 0
    for i in range(n-1):
        max_index = i
        for j in range(i+1, n):
            if data[j] > data[max_index]:
                max_index = j
        max_value = data.pop(max_index)
        data.insert(i, max_value)
        swap1 += 1
        if not swap1:
            break
    max_value = python_data.pop(max_index)
    python_data.insert(i, max_value)
    return data, swap1

data_bubble = python_data.copy()
hasil, swap = bubble_sort(data_bubble)
data_select = python_data.copy()
hasil1, swap1 = select_sort(data_select)
print("Hasil Bubble Sort (Besar -> Kecil):", hasil) 
print("Jumlah Swap Bubble Sort:", swap)
print('')
print("Hasil Selection Sort (Kecil -> Besar):", hasil1)
print("Jumlah Swap Selection Sort:", swap1)