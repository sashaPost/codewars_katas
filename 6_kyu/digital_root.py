
def summer(s):
    sum = 0
    for i in str(s):
        sum += int(i)
    return sum
    
def digital_root(n):
    total = 0
    if len(str(n)) > 1:
        total = summer(n)
    else:
        return n
    while len(str(total)) > 1:
        total = summer(total)
    return total



print(digital_root(16))
print(digital_root(942))
print(digital_root(132189))
print(digital_root(493193))
