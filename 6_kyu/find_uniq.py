
def find_uniq(arr):
    ls = dict()
    for i in arr:
        if i not in ls:
            ls[i] = 1
        else: 
            ls[i] += 1
    for key, value in ls.items():
        if value == 1:
            return key
        
        
        
print(find_uniq([ 1, 1, 1, 2, 1, 1, 3 ]))
print(find_uniq([ 0, 0, 0.55, 0, 0 ]))
