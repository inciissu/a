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
