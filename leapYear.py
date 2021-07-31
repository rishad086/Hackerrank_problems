def is_leap(year):
    if year%4==0 and year % 400==0 and year  %100 != 0:
        return True


    elif year%4==0 and year  %100 != 0:

        return True
    elif year % 100 == 0 and year % 400 ==0:
        return False
    else:
        return False



    # Write your logic here


year = int(input())
years=is_leap(year)
print(years)