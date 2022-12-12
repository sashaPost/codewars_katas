
def is_isogram(string):
    items = list()
    for letter in string:
        if letter.lower() not in items:
            items.append(letter.lower())
        else:
            return False
    if len(items) == len(string):
        return True
    
    
    
# print(is_isogram("Dermatoglyphics"))
# print(is_isogram("aba"))
# print(is_isogram("moOse"))
