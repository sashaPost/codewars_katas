
def disemvowel(string_):
    vowels_low = "aeiou"
    all_vow = vowels_low.upper() + vowels_low
    for i in string_:
        if i in all_vow:
            string_ = string_.replace(i, '')
    return string_
    
    
    
print(disemvowel("First fixed test"))
print(disemvowel("This website is for losers LOL!"))
