# Fibonacci series
num = int(input("Enter the number: "))
a = 0
b = 1
for i in range(num):
  print(a)
  c = a + b
  a = b
  b = c