
def likes(names):
    if len(names) >= 4:
        how_much = str(len(names) - 2)
        return f"{names[0]}, {names[1]} and {how_much} others like this"
    else:
        if len(names) == 3:
            return f"{names[0]}, {names[1]} and {names[-1]} like this"
        elif len(names) == 2:
            return f"{names[0]} and {names[-1]} like this"
        elif len(names) == 1:
            return f"{names[0]} likes this"
        else:
            return "no one likes this"
