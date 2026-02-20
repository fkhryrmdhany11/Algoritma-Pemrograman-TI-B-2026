def hitung_rata_rata():
    while True:
        try:
            jumlah = int(input("Masukkan jumlah nilai: "))
            if jumlah <= 0:
                print("Jumlah harus lebih dari 0.")
                continue
            break
        except ValueError:
            print("Input harus berupa angka.")

    total = 0

    for i in range(jumlah):
        while True:
            try:
                nilai = float(input(f"Masukkan nilai ke-{i+1}: "))
                total += nilai
                break
            except ValueError:
                print("Nilai harus berupa angka.")

    rata_rata = total / jumlah
    print(f"Rata-rata nilai adalah: {rata_rata}")

hitung_rata_rata()