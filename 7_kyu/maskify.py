
def maskify(cc):
    if len(cc) > 4:
        return ('#' * (len(cc) - 4) +str(cc[-4:]))  
    else:
        return cc
    
    
    
# print(maskify("What was the name of your first pet?"))
