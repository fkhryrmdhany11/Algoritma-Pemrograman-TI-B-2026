def penambahan(a,b):
    hasil = a + b
    print(hasil)
    return hasil

def pengurangan(a,b):
    hasil = a - b
    print(hasil)
    return hasil

def perkalian(a,b):
    hasil = a * b
    print(hasil)
    return hasil

def pembagian(a,b):
    if b == 0:
        print('Pembagian tidak dapat dilakukan karena pembagi bernilai 0')
    else:
        hasil = a / b
        print(hasil)
        return hasil

def modulus(a,b):
    print(a % b)

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    print(n)