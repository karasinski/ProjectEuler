import numpy as np
import re


def natural_sort(l):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(l, key=alphanum_key)


names = np.loadtxt('data/p022_names.txt', delimiter=',', dtype=str)
names = [n.replace('"', '') for n in names]
sorted_names = natural_sort(names)

letters = {}
for i in range(65, 65 + 26):
    letters[chr(i)] = i - 65 + 1


total_score = 0
for index, name in enumerate(sorted_names):
    score = 0
    for letter in name:
        score += letters[letter]
    score *= index + 1

    total_score += score

print(total_score)
