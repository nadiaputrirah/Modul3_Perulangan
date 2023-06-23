print("==== PROGRAM JUMLAH TOTAL BILANGAN ===")
bilangan = int(input("Masukkan bilangan = "))
total = 0
print("Total Nilai=", end="")
for i in range(bilangan, 0, -1):
    total += i
    print(i, end="")
    if i != 1:
        print(" + ", end="")
print(" = {}".format(total))

