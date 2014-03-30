import math

def triangle_number(n):
  return int(n*(n+1)/2)

def NumberOfDivisors(number):
  nod = 0
  sqrt = int(math.sqrt(number))

  for i in range(1, sqrt):
    if number % i == 0:
      nod += 2;
  if sqrt * sqrt == number:
      nod -= 1;
  return nod;

i = 0
while (True):
  i += 1
  num = triangle_number(i)
  div = NumberOfDivisors(num)
  if div >= 500:
    print('Winner')
    print(i, num, div)
    break
