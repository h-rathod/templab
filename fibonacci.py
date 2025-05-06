def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)

n = int(input("Enter a number: "))
if n<0:
  print("Enter positive number")
else:
  print("Fibonacci sequence:")
  for i in range(n + 1):
      print(fibo(i))
    
# another way 

n = int(input("Enter a number: "))

if n < 0:
    print("Enter a positive number")
else:
    print("Fibonacci sequence:")
    a, b = 0, 1
    for _ in range(n + 1):
        print(a)
        a, b = b, a + b
