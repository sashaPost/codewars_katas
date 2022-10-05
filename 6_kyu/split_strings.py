def solution(s):
    lst = list()
    if len(s) % 2 == 0:        
        lst += [ s[index] + s[index + 1] for index in range(0, len(s), 2) ]
    else:
        s += "_"
        lst += [ s[index] + s[index + 1] for index in range(0, len(s), 2) ]
    return lst
    
    

print(solution('abc'))
print(solution('abcdef'))