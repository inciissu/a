"""""
number = eval(input("enter an integer :"))
isPrime =True
i = 2
while i < number and isPrime:
  if number % i ==0:
    isPrime= False
    i  += 1

    print("i is",i)

    if isPrime:
      print(number, "is prime")
    else:
      print(number, "is not prime")
"""
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
n = int(input("n sayısını giriniz: "))
fibonacci(n)
