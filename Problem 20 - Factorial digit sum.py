import math

def sum_of_digits(n):
  num = str(math.factorial(n))
  num = [int(num[i:i+1]) for i in range(0, len(num), 1)]
  print(sum(num))

sum_of_digits(100)