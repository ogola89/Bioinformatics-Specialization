def MinimumSkew(Genome):
    max_skew = []
    skew = {}
    skew[0] = 0
    print ('Skew starting at 0.')
    for i in range(len(Genome)):
        if Genome[i] == 'G':
            skew[i+1] = skew[i]+1
            print ('G is the Nucleotide. Skew is increasing to '+ str(skew[i+1])
        elif Genome[i] == 'C':
            skew[i+1] = skew[i] -1
            print ('C is the Nucleotide. Skew is decreasing to '+ str(skew[i+1])
        else:
            skew[i+1] = skew[i]
            print ('T or A is the Nucleotide. Skew is staying as '+ str(skew[i+1])
    skew2 = list(skew.values())
    m = max(skew)
    for i in range(len(skew2)):
        if skew2[i] == m:
            max_skew.append(i)
    return max_skew

print (MinimumSkew('GCATACACTTCCCAGTAGGTACTG'))