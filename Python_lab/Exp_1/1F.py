# pattern drawing
terms = int(input("Enter the number of terms: "))

for i in range(terms):
  for j in range(i+1):
    print(chr(i+65), end="")
  print()

for i in range(terms,0,-1):
  for j in range(terms-i):
    print(" ", end="")
  for j in range(i):
    print("*", end="")
  print()

for i in range(terms):
  for j in range(terms-i):
    print(" ", end="")
  for j in range(i+1):
    print(j+1, end="")
  for j in range(i,0,-1):
    print(j, end="")
  print()

for i in range(terms):
  for j in range(terms-i):
    print(" ", end="")
  for j in range(i+1):
    print(" *", end="")
  print()