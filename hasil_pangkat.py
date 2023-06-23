print("===== HITUNG HASIL PANGKAT =====")
def hitung_pangkat(bilangan, pangkat):
    hasil = 1

    for _ in range(pangkat):
        hasil *= bilangan

    return hasil

# Contoh penggunaan
bilangan = int(input("Masukkan bilangan: "))
pangkat = int(input("Masukkan pangkat: "))

hasil_pangkat = hitung_pangkat(bilangan, pangkat)
print("Hasil pangkat:", hasil_pangkat)