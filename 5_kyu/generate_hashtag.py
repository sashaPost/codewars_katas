
def generate_hashtag(s):
    res_str = "#"
    if len(s) == 0:
        return False
    else:
        s_ls = s.split(' ')
        for i in s_ls:
            res_str += i.capitalize()
        if len(res_str) > 140:
            return False
        else:
            return res_str



print(generate_hashtag(''))
print(generate_hashtag('Do We have A Hashtag'))
print(generate_hashtag('Codewars'))
