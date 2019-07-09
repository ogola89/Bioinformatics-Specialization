#Computing Frequencies

def ComputingFrequencies (Text,k):
    for in range (0,4^k-1):
        FrequencyArray[i] = 0
    for i in range (0,len(Text)-k):
        Pattern = Text(i:i+k)
        j = PatternToNumber(Pattern)
        FrequencyArray[j] = FrequencyArray[j+] +=1
    return FrequencyArray



# Clump Finding Algorithm

def ClumpFinding(Genome, k,L,t):
    FrequentPatterns = []
    for i in range (0, (4^k-1)):
        Clump[i] = 0
    for i in range (0,len(Genome)-L)):
        Text = Genome[i:i+L]
        FrequencyArray = ComputingFrequencies(Text,k)
        for i in range (0,4^k-1):
            if FrequencyArray[i] >= t:
                Clump[i] += 1
    for i in range (0,4^k-1):
        if Clump[i] = 1
        Pattern = NumberToPattern(i,k)
        Pattern += FrequentPatterns
    return FrequentPatterns
