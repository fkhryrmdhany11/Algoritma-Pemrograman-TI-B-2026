def jumlah_digit(n):
    if n < 10:
        return n
    hasil = n % 10 + jumlah_digit(n // 10)
    return hasil

print(jumlah_digit(1234))