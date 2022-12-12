
def accum(s):
    
    s_list = [let for let in s]
    
    res_list = list()
    for i in range(len(s_list)):
        res_list += s_list[i].upper() + s_list[i].lower()*i
        
    res_str = res_list[0]
    
    for i in res_list[1:]:
        if i.isupper() == True:
            res_str += "-" + i
        else:
            res_str += i
    
    return res_str
     
    
    
print(accum("ZpglnRxqenU")) #"Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu"
print(accum("NyffsGeyylB")) #"N-Yy-Fff-Ffff-Sssss-Gggggg-Eeeeeee-Yyyyyyyy-Yyyyyyyyy-Llllllllll-Bbbbbbbbbbb"
print(accum("MjtkuBovqrU")) #"M-Jj-Ttt-Kkkk-Uuuuu-Bbbbbb-Ooooooo-Vvvvvvvv-Qqqqqqqqq-Rrrrrrrrrr-Uuuuuuuuuuu"
print(accum("EvidjUnokmM")) #"E-Vv-Iii-Dddd-Jjjjj-Uuuuuu-Nnnnnnn-Oooooooo-Kkkkkkkkk-Mmmmmmmmmm-Mmmmmmmmmmm"
print(accum("HbideVbxncC")) #"H-Bb-Iii-Dddd-Eeeee-Vvvvvv-Bbbbbbb-Xxxxxxxx-Nnnnnnnnn-Cccccccccc-Ccccccccccc"
