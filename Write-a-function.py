def is_leap(year):
    leap = False
    
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            leap = False
        elif year % 100 == 0 and year % 400 == 0:
            leap = True
        else:
            leap = True 
    
    return leap
