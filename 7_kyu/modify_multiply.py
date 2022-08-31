
def modify_multiply(st, loc, num):
    
    ls = st.split(' ')
    
    res = (ls[loc] + "-") * num
    
    return res[0:-1]



print(modify_multiply("This is a string",3 ,5))
