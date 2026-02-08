def rata_rata(nilai):
    return sum(nilai)/len(nilai) if len(nilai) != 0 else print('data kosong')

data = [80, 75, 90, 60, 85]
print(rata_rata(data))