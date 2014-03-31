import math

def log10fib(n):
  golden = (1 + math.sqrt(5))/2
  return n*math.log10(golden) - 0.5*math.log10(5)

i = 0
while (True):
  i += 1
  
  if log10fib(i) > 999:
    print(i)
    break