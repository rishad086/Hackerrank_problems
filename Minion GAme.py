def minion_game(string):
    p1=0
    p2=0
    for i in range(len(string)):
        if string[i] in "AEIOU":
            p1=p1+len(string)-i
        else:
            p2=p2+len(string)-i

    if p1 > p2:
        print("Kevin", p1)
    elif p1 < p2:
        print("Stuart", p2)
    elif p1 == p2:
        print("Draw")
    else:
        print("Draw")



s = input()
minion_game(s)