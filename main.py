n  = int(input("Enter an integer greater than 1: "))
i = 0
while n > 1:
  i = i + 1
  if n%2 == 0: #i.e. n is even
    n = n/2
  else: # i.e. n is otherwise, (odd)
    n = 3*n + 1
  print(n)
print(f'The total number of iterations required to reach 1 is: {i}')