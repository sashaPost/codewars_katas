def high(x):
    x_list = x.split()
    word_scores = dict()
    for word in x_list:
        word_scores[word] = sum([ ord(letter) - 96 for letter in word ])
    max_score = max(word_scores, key=word_scores.get)
    return max_score
    
    

print(high('man i need a taxi up to ubud'))