
def find_short(s):
    word_dict = dict()
    str_list = s.split()
    for i in str_list:
        word_dict[i] = len(i)
    l = min(word_dict.values())
    return l



print(find_short("bitcoin take over the world maybe who knows perhaps"))
print(find_short("turns out random test cases are easier than writing out basic ones"))
print(find_short("lets talk about javascript the best language"))
print(find_short("i want to travel the world writing code one day"))
print(find_short("Lets all go on holiday somewhere very cold"))   
print(find_short("Let's travel abroad shall we"))
