def swap_case(s):
    str=""
    for x in s:
        if (x.isupper()==True):
            str=str+x.lower()
        elif (x.islower()==True):
            str=str+x.upper()
        else:
            str=str+x
    return str


s = input()
result = swap_case(s)
print(result)