def ReverseComplement(Pattern):
    x = []
    for i in Pattern:
        if i == "C":
            x += "G"
        elif i == "G":
            x += "C"
        elif i == "T":
            x += "A"
        elif i == "A":
            x += "T"
    return "".join(x[::-1])

