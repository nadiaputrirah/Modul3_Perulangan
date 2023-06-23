print("====PROGRAM MENCARI FPB====")

#mendefinisikan fungsi
def menghitung_fpb(a, b):
    #memilih bilangan yang paling kecil
    if a > b:
        terkecil = b
    else:
        terkecil = a
    for i in range(1, terkecil+1):
        if((a % i == 0) and (b % i ==0)):
            fpb = i
    return fpb


bilangan1 =int(input("Masukkan bilangan pertama: "))
bilangan2 = int(input("Masukkan bilangan kedua: "))

hasil_fpb = menghitung_fpb(bilangan1, bilangan2)
print("Faktopr persekutuan terbsesar = ", hasil_fpb)