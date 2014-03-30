import math

def SumOfDivisors(number):
  total = 0

  for i in range(1, number):
    if number % i == 0:
      total += i
  # print(number, total)
  return total

def sum_amicable_numbers(k):
  print('Pairs of amicable numbers below', k)
  l = []
  for i in range(1, k+1):
    if i not in l:
      i_d = SumOfDivisors(i)
      j_d = SumOfDivisors(i_d)
      if i == j_d and i_d != j_d:
        l.append(i_d)
        l.append(j_d)
        print(i_d, j_d)
  print('Sum is', sum(l))

sum_amicable_numbers(10000)
# SumOfDivisors(220)
# SumOfDivisors(284)