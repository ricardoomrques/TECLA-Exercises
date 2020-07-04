def special_day(day,month):
    months_with_31_days = [1,3,5,7,8,10,12]
    months_with_30_days = [4,6,9,11]
    if (month in months_with_31_days and 0 < day < 32):
        if (month > 1): return "posterior"
        elif (day == 30): return "especial"
        else: return "anterior"
    elif (month == 2 and day < 29):
        return "posterior"
    elif (month in months_with_30_days and day < 31):
        if (month > 1): return "posterior"
        elif (day == 30): return "especial"
        else: return "anterior"
    return "invalida"

print(special_day(25,1))
print(special_day(18,8))
print(special_day(29,2))
