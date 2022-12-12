
def spin_words(sentence):
    
    sen_lst = sentence.split()
    
    for ind in range(len(sen_lst)):
        if len(sen_lst[ind]) >= 5:
            sen_lst[ind] = sen_lst[ind][::-1]

    res_str = str()
    for i in sen_lst[0:-1]:
        res_str += (i + " ")
    res_str = res_str + sen_lst[-1]
    return res_str
    
    
    
print(spin_words("Hey fellow warriors"))
print(spin_words("This sentence is a sentence"))
