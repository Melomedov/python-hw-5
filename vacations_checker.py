from  vacations_calendar import calendar

# for key in calendar.keys():
# 	print(key)

def check(date_str):
    global calendar    
    for key in calendar:
        if key == date_str:
            return calendar[key]
       

print(check('27/07/2022'))
print(check('28/07/2022'))
print(check('28/07/2020'))