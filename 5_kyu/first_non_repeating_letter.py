
def first_non_repeating_letter(string):
    low_str = string.lower()
    res = str()
    for let in low_str:
        if low_str.count(let) == 1:
            res += string[low_str.index(let)]
    if len(res) != 0:
        return res[0]
    else:
        return ''
   


print(first_non_repeating_letter('a'))
print(first_non_repeating_letter('stress'))
print(first_non_repeating_letter('moonmen'))
