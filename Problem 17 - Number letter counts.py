one = 'one'
two = 'two'
three = 'three'
four = 'four'
five = 'five'
six = 'six'
seven = 'seven'
eight = 'eight'
nine = 'nine'
ten = 'ten'
eleven = 'eleven'
twelve = 'twelve'
thirteen = 'thirteen'
fourteen = 'fourteen'
fifteen = 'fifteen'
sixteen = 'sixteen'
seventeen = 'seventeen'
eighteen = 'eighteen'
nineteen = 'nineteen'
twenty = 'twenty'
thirty = 'thirty'
forty = 'forty'
fifty = 'fifty'
sixty = 'sixty'
seventy = 'seventy'
eighty = 'eighty'
ninety = 'ninety'
hundred = 'hundred'
thousand = 'thousand'

def check_and(n, word, num, string):
  if n >= num:
    word += string
    n -= num
    if n > 0:
      word += ' and '
  return n, word

def check(n, word, num, string):
  if n >= num:
    word += string
    n -= num
    if n > 0:
      word += ' '
  return n, word

def write_it_out(n):
  word = ''
  while n > 0:
    n, word = check_and(n, word, 1000, one   + ' ' + thousand)
    n, word = check_and(n, word,  900, nine  + ' ' + hundred)
    n, word = check_and(n, word,  800, eight + ' ' + hundred)
    n, word = check_and(n, word,  700, seven + ' ' + hundred)
    n, word = check_and(n, word,  600, six   + ' ' + hundred)
    n, word = check_and(n, word,  500, five  + ' ' + hundred)
    n, word = check_and(n, word,  400, four  + ' ' + hundred)
    n, word = check_and(n, word,  300, three + ' ' + hundred)
    n, word = check_and(n, word,  200, two   + ' ' + hundred)
    n, word = check_and(n, word,  100, one   + ' ' + hundred)
    n, word = check    (n, word,   90, ninety)
    n, word = check    (n, word,   80, eighty)
    n, word = check    (n, word,   70, seventy)
    n, word = check    (n, word,   60, sixty)
    n, word = check    (n, word,   50, fifty)
    n, word = check    (n, word,   40, forty)
    n, word = check    (n, word,   30, thirty)
    n, word = check    (n, word,   20, twenty)
    n, word = check    (n, word,   19, nineteen)
    n, word = check    (n, word,   18, eighteen)
    n, word = check    (n, word,   17, seventeen)
    n, word = check    (n, word,   16, sixteen)
    n, word = check    (n, word,   15, fifteen)
    n, word = check    (n, word,   14, fourteen)
    n, word = check    (n, word,   13, thirteen)
    n, word = check    (n, word,   12, twelve)
    n, word = check    (n, word,   11, eleven)
    n, word = check    (n, word,   10, ten)
    n, word = check    (n, word,    9, nine)
    n, word = check    (n, word,    8, eight)
    n, word = check    (n, word,    7, seven)
    n, word = check    (n, word,    6, six)
    n, word = check    (n, word,    5, five)
    n, word = check    (n, word,    4, four)
    n, word = check    (n, word,    3, three)
    n, word = check    (n, word,    2, two)
    n, word = check    (n, word,    1, one)
  return word

full_string = ''
for i in range(1, 1001):
  string = write_it_out(i).replace(" ", "")
  full_string += string

print(len(full_string))
