def PatternToNumber(Pattern):
  Pattern = Pattern[::-1]
  q = len(Pattern) - 1
  Number = 0
  while q >= 0 :
    if Pattern[q] == 'A':
      num = 0
    if Pattern[q] == 'C':
      num = 1
    if Pattern[q] == 'G':
      num = 2
    if Pattern[q] == 'T':
      num = 3
    Number += (num * (4**q))
    q -= 1
  return(Number)

Pattern = input()
print(PatternToNumber(Pattern))
