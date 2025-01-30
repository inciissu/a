rows = 9  # Toplam satır sayısı
start = 1  # Sol sütunda başlayan sayı

for i in range(0,10)(1, rows + 1):  # Satır döngüsü
    for j in range(start, start + i):  # Sütun döngüsü
        print(j * i, end=" ")  # j'nin i ile çarpımını yazdır
    start += 1  # Sol sütun sayısını bir artır
    print()  # Bir sonraki satıra geç