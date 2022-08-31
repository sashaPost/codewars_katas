
def anagrams(word, words):
    sortedSample = sorted(word)    
    anaList = [ an for an in words if sorted(an) == sortedSample ]
    return anaList
    


print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
