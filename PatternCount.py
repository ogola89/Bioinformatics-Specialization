#Algorithm to count the frequency of a pattern within
#a given text (DNA String)

def PatternCount (Text, Pattern):
    count = 0
    for i in range (0,len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count += 1
    return count
        