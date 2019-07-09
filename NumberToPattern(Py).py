def NumberToPattern(number,length):
    pattern = []
    for i in range ( 0,length):
        division = number % (4^(length-i))
        if division == 0:
            pattern.append('A')
        elif division == 1:
            pattern.append('C')
        elif division == 2:
            pattern.append('G')
        elif division == 3:
            pattern.append('T')
        number = number - division * (4^(length-i))

    return "".join(pattern)
