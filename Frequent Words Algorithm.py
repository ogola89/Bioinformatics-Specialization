#An algorithm to find the most frequent k-mers in a string of DNA

def FrequentWords(Text, k):
    dict = {}
    for i in range (0,len(Text)-1):
        if not Text[i:i+k] in dict:
            dict[Text[i:i+k]] = 1
        elif Text[i:i+k] in dict:
            dict[Text[i:i+k]] +=1
    
    maxv = max(dict.values())
    mynewdict ={}
    for key, value in dict.items():
      if value == maxv:
        mynewdict[key] = value
    
    return (mynewdict)


