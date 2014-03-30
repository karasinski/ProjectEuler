def is_even(n):
  return n % 2 == 0

def collatz(n):
  if n == 1:
    return 1
  elif is_even(n):
    return 1 + collatz(n/2)
  else:
    return 1 + collatz(3*n + 1)

longest_length = 0
longest_i = 0
for i in range(1, 1000000):
  num = collatz(i)
  if num > longest_length: 
    longest_length = num
    longest_i = i

print(longest_i, longest_length)