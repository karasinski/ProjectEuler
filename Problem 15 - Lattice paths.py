import math

def nCr(n,r):
  f = math.factorial
  return int(f(n) / f(r) / f(n-r))

print(nCr(40, 20))