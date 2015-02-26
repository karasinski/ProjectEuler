from __future__ import division
from decimal import Decimal, getcontext
import re

getcontext().prec = 2000
longest_recurring_d, max_length = 0, 0
for d in range(1, 1000):
    decimal = str(1 / Decimal(d))
    pattern = re.search(r"^[0-9]\.[0-9]*([0-9]{7,}?)(\1+)[0-9]*?$", decimal)
    if pattern is not None:
        length = len(pattern.group(1))
        if length > max_length:
            max_length = length
            longest_recurring_d = d

print(longest_recurring_d)
