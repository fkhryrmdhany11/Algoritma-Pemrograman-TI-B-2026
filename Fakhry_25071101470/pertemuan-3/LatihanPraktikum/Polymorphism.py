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