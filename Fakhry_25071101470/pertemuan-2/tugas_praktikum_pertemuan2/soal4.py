def pangkat(a, b):
    if b == 0:
        return 1
    hasil = a * pangkat(a, b-1)
    return hasil

print(pangkat(2, 5))