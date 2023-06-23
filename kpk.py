print("==== MENGHITUNG KPK ====")
def cari_kpk(a, b):
    # Menentukan bilangan terbesar antara a dan b
    bil_max = max(a, b)

    while True:
        if bil_max % a == 0 and bil_max % b == 0:
            kpk = bil_max
            break
        bil_max += 1

    return kpk

bilangan1 = int(input("Masukkan bilangan bulat pertama: "))
bilangan2 = int(input("Masukkan bilangan bulat kedua: "))

hasil_kpk = cari_kpk(bilangan1, bilangan2)
print("KPK = ", hasil_kpk)
