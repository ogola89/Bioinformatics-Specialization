def PatternToNumber (Pattern): #Returns the number of k-mer from the k-mer list
    i = 0
    Number = []
    while i < len(Pattern):
        if Pattern[i] == 'C':
            Number = Number + 1 * 4 ** (len(Pattern) - i - 1)
        if Pattern[i] == 'G':
            Number = Number + 2 * 4 ** (len(Pattern) - i - 1)
        elif Pattern[i] == 'T':
            Number = Number + 3 * 4 ** (len(Pattern) - i - 1)
        i += 1
    return Number

print (PatternToNumber ('AGCT'))
