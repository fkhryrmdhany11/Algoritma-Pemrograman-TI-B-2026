class Mahasiswa:
  def __init__(self, nilai):
    self.__nilai = nilai

  def get_nilai(self):
    return self.__nilai

  def set_nilai(self, nilai):
    if nilai > 0:
      self.__nilai = nilai
    else:
      print("Nilai tidak valid")

m1 = Mahasiswa(70)
print(m1.get_nilai())

m1.set_nilai(90)
print(m1.get_nilai())