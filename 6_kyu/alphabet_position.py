def alphabet_position(text):
    low_alph_list = [ i for i in range(97, 123) ]
    res_list = [ ord(sign) - 96 for sign in text.lower() if ord(sign) in low_alph_list ]
    index_str = str()
    for i in res_list:
        index_str += str(i) + " "
    return index_str[0:-1]
        
    

print(alphabet_position("The sunset sets at twelve o' clock."))