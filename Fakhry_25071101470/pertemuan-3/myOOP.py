class Produk:
    def __init__(self, nama_produk, harga):
        self.nama_produk = nama_produk
        self.harga = harga
    def info_produk(self):
        print(f'Nama: {self.nama_produk} Harganya {self.harga}')

class ProdukElektronik(Produk):
    def __init__(self, nama_produk, harga, garansi):
        super().__init__(nama_produk, harga)
        self.garansi = garansi
    def Info_produkElektronik(self):
        print(f'{self.nama_produk} Seharga {self.harga} garansi {self.garansi} tahun')
        return self.nama_produk, self.harga, self.garansi

class ProdukMakanan(Produk):
    def __init__(self, nama_produk, harga, kadaluarsa):
        super().__init__(nama_produk, harga)
        self.kadaluarsa = kadaluarsa
    def Info_produkMakan(self):
        print(f'{self.nama_produk} Seharga {self.harga} kadarluarsa {self.kadaluarsa}')
        return self.nama_produk, self.harga, self.kadaluarsa

elektronik = ProdukElektronik('TV', "3.000.000", 2)
makanan = ProdukMakanan('Roti', "15.000", 2026)

elektronik.Info_produkElektronik()
makanan.Info_produkMakan()

#---------------------------------------------------------------------------------
class notifikasi:
    def __init__(self, pesan):
        self.pesan = pesan
    def kirim(self):
        return self.pesan

class email(notifikasi):
    def kirim(self):
        print("Mengirim notifikasi melalui Email")
        

class SMS(notifikasi):
    def kirim(self):
        print("Mengirim notifikasi melalui SMS")

test = email('Manusia')
test1 = SMS('Manusia')

print(test1.kirim())
print(test.kirim())

#---------------------------------------------------------------------------------
class Mahasiswa:
  def __init__(self, nilai):
    self.__nilai = nilai

  def get_age(self):
    return self.__nilai

  def set_age(self, nilai):
    if nilai > 0:
      self.__nilai = nilai
    else:
      print("Age must be positive")

m1 = Mahasiswa(70)
print(m1.get_age())

m1.set_age(90)
print(m1.get_age())