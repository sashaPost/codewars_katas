def square_digits(num):
    
    str_num = str(num)
    
    res_str = str()
    for let in str_num:
        res_str += str(int(let) ** 2)
    
    return int(res_str)



print(square_digits(9119))
print(square_digits(0))