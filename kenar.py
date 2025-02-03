kenar1 = int(input("Birinci kenarı girin: "))
kenar2 = int(input("İkinci kenarı girin: "))
kenar3 = int(input("Üçüncü kenarı girin: "))

if kenar1 == kenar2 == kenar3:
    print("Bu bir eşkenar üçgendir.")
elif kenar1 == kenar2 or kenar1 == kenar3 or kenar2 == kenar3:
    print("Bu bir ikizkenar üçgendir.")
else:
    print("Bu bir çeşitkenar üçgendir.")