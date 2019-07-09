def PatternMatching(Pattern, Genome):
    x = []
    g = len(Genome)
    p = len(Pattern)
    for i in range (0, (g-p)+1):
        if Genome[i:i+p] ==  Pattern:
            x.append(i)
    return x
