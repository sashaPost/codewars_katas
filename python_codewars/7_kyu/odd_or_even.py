

def odd_or_even(arr):
    
    count = 0
    
    for i in arr:
        count += i
    
    if count % 2 == 0:
        return "even"
    else:
        return "odd"
    
    
    
print(odd_or_even([0, 1, 2]))
