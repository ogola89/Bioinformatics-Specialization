#Create hamming distance algorithm to allow matching of patterns that are approximate matches in later code
#Hamming distance compares the differences between the two inputs, preferably for comparing gene sequences
def HammingDistance (seq1,seq2):
    hamming_distance = 0
    for i in range (0, len(seq1)):
        if seq1[i] != seq2[i]:
            hamming_distance +=1
    return hamming_distance

# This algorithm compares counts the frequency of a pattern within a Genome(Text). However, due to the hamming distance algorithm above,
# it is possible to stipulate a variation of the pattern to a section of genome, by a certain amount of mismatches (d)
def ApproximatePatternCount(Genome, Pattern, d=0):
    while d > len(Pattern):
        d = int(input("Please choose a mismatch of less than " + str(len(Pattern))))
    count = 0 # initialize count variable
    for i in range (0, len(Genome)-(len(Pattern)-1)):
        f = Genome[i:i+(len(Pattern))]
        if int(HammingDistance(Pattern,f)) <= d:
            count += 1
    # your code here
    return count

#Example below prints 6 approximate matches
print (ApproximatePatternCount('CATGCCATTCGCATTGTCCCAGTGA', 'CCC',1))

