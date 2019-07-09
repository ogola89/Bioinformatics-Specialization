def ClumpFinding(genome, k, L, t):
    sequence_set={}
    slide_window = L
    counter = 0
    while slide_window != len(genome):
        for i in range (counter,L):
            window = genome[i:i+k]
            if window not in sequence_set:
                sequence_set[window]=1
            elif window in sequence_set:
                sequence_set[window]+=1
        slide_window += 1
        print (window)
        key_values={}
        counter +=1
        print("Counter is now starting at " + str(counter))
        print (genome[counter:L])
        print ("Slide window size is now " + str(slide_window))

    for key,value in sequence_set.items():
        if value == t:
            key_values[key] = value
    print (key_values)
    print (sequence_set)

ClumpFinding (genome='ATCGTGCTGATGCTGCTGATGCTGATGCTGATGCTGATAAGGCTGCGATGCAT', k=4,L=10,t=2)

