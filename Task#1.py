def most_wanted_letter(s):
    letters = {}
    count = 0
    wanted_letter = ""
    flag = False
    for i in s.lower():
        if i.isalpha():
            flag = True
            if i in letters:
                letters[i] += 1
            else:
                letters[i] = 1
    if not flag:
        return "There are no letters in the string"        
    
    for k, v in letters.items():
        if v > count:
            count = v
            wanted_letter = k
    return f"Most wanted letter is {wanted_letter}"   

# s = input()
# print(most_wanted_letter(s))
print(most_wanted_letter("......HeLlo......"))
print(most_wanted_letter("String ssss ttAAds TTTTTTT"))
print(most_wanted_letter("!@#$%^&*(*&^%$#@@#$%^&*DFGBQQQQQQQQqqqrrrrrrrr"))
print(most_wanted_letter("!@#$%^&*543234%^&*%$#@345677^%$#@#$%^&"))
print(most_wanted_letter("....пррррривет..."))
print(most_wanted_letter("....Tschüüüüüüüss!..."))
      
    
        