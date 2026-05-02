struktur = {
    "Skripsi_Aqil": {
        "Bab_1": {
            "pendahuluan.docx": 45,
            "latar_belakang.docx": 62
        },
        "Bab_2": {
            "landasan_teori.docx": 118,
            "referensi": {
                "paper_A.pdf": 340,
                "paper_B.pdf": 210
            }
        },
        "Bab_3": {
            "metodologi.docx": 89,
            "diagram": {
                "flowchart.png": 512,
                "erd.png": 278,
                "arsitektur": {
                    "sistem.png": 430
                }
            }
        },
        "sidang": {
            "presentasi.pptx": 2048,
            "catatan_revisi.txt": 15
        },
        "README.txt": 8
    }
}

def total_ukuran(folder: dict) -> int:
    total = 0
    for key, value in folder.items():
        if isinstance(value, dict):
            total += total_ukuran(value)
        else:
            total += value
    return total

def hitung_file(folder: dict) -> int:
    count = 0
    for key, value in folder.items():
        if isinstance(value, dict):
            count += hitung_file(value)
        else:
            count += 1
    return count

def cari_terbesar(folder: dict) -> tuple:
    file_terbesar = None
    ukuran_terbesar = 0
    
    for key, value in folder.items():
        if isinstance(value, dict):
            nama, ukuran = cari_terbesar(value)
            if ukuran > ukuran_terbesar:
                file_terbesar = nama
                ukuran_terbesar = ukuran
        else:
            if value > ukuran_terbesar:
                file_terbesar = key
                ukuran_terbesar = value
    
    return (file_terbesar, ukuran_terbesar)

def tampilkan_tree(folder: dict, nama: str = "root", level: int = 0):
    if level == 0:
        print("📁 " + nama)
    else:
        indent = "  " * (level - 1)
        print(indent + "📁 " + nama)
    
    for key, value in folder.items():
        if isinstance(value, dict):
            tampilkan_tree(value, key, level + 1)
        else:
            indent = "  " * level
            print(f"{indent}📄 {key} ({value} KB)")


total = total_ukuran(struktur["Skripsi_Aqil"])
jumlah = hitung_file(struktur["Skripsi_Aqil"])
nama_file, ukuran_file = cari_terbesar(struktur["Skripsi_Aqil"])

print("=" * 50)
print("        PROGRAM EXPLORER FOLDER SKRIPSI")
print("=" * 50)

print(f"Total ukuran skripsi: {total} KB")
print(f"Jumlah file: {jumlah} file")
print(f"File terbesar: {nama_file} ({ukuran_file} KB)")
tampilkan_tree(struktur)