DAFTAR_ANGKA = [23, 67, 4, 89, 15, 42, 73, 31, 58, 9]
DataFiks = []

# === BAGIAN A ===
# Untuk menbak angka rahasia dari angka tebakan
def tebak_angka(angka_rahasia, maks_percobaan = 7):
    global sisa_percobaan
    for i in range(maks_percobaan):
        tebakan = int(input('masukkan angka (rentang angka 1-100): '))
        if tebakan < angka_rahasia:
            print('Terlalu Kecil')
        elif tebakan > angka_rahasia:
            print('Terlalu Besar')
        else:
            print('Benar!')
            berhasil = True
            break
        maks_percobaan -= 1
    sisa_percobaan = maks_percobaan
    if sisa_percobaan == 0:
        print('Percobaan Habis')
        berhasil = False

# Untuk mengihitung skor dari hasil tebakan
def hitung_skor(berhasil, sisa_percobaan):
    if berhasil == True:
        sisa_percobaan = sisa_percobaan * 10
    else:
        return 0

# Untuk menggabungkan fungsi
def main_satu_ronde(nama, nomor_ronde):
    global angka_rahasia
    global DataFiks
    angka_rahasia = (DAFTAR_ANGKA[nomor_ronde % len(DAFTAR_ANGKA)])
    print('Nomor Ronde: ')
    berhasil = tebak_angka(angka_rahasia, 7)
    data = []
    data.append(nama)
    data.append(hitung_skor(berhasil, sisa_percobaan))
    DataFiks.append(data)

# === BAGIAN B ===
# Untuk menampilkan riwayat pemain
def tampilkan_riwayat(riwayat):
    if len(riwayat):
        print('Nomor | Nama | Skor |')
        for i in range(len(riwayat)):
            print(f'No.{i+1} | Nama: {DataFiks[i][0]} | Skor: {DataFiks[i][1]}')
    else:
        print('Belum ada Riwayat')

# === BAGIAN C ===
def selection_sort_riwayat(riwayat):
    pass
def tampilkan_leaderboard(riwayat):
    pass

main_satu_ronde('Fakhry', 10)
tampilkan_riwayat()