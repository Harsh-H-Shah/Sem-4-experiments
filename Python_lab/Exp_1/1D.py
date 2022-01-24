for i in range(1,1000):
  temp = i
  comp = 0
  while i:
    comp += (i % 10) ** 3
    i //= 10
  if temp == comp:
    print(temp)
    