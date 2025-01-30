''' 
sayi = int(input("Bir sayi giriniz: "))
if sayi % 2 == 0:
    sonuc = "cift"
    print(sayi, sonuc, "bir sayidir")
else:
    sonuc = "tek"
    print(sayi, sonuc, "bir sayidir")
'''
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
n = int(input("n sayısını giriniz: "))
fibonacci(n)
