def sum_of_digits(n, k):
  num = str(pow(n, k))
  num = [int(num[i:i+1]) for i in range(0, len(num), 1)]
  print(sum(num))

sum_of_digits(2, 1000)
