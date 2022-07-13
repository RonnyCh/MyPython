from datetime import datetime, timedelta

# to figure out now() like excel

import calendar

x = datetime.now()
yr = x.year
mth = str(x.month - 1)
day = calendar.monthrange(x.year, x.month - 1)
day = str(day[1])

if len(mth) == 1:
    mth = '0' + str(mth)
else:
    mth = str(mth)

str(x.year) + '-' + mth + '-' + day



m = pd.Period(x,freq='M').end_time.date()



# you can print year, month, hour, minutes etc

print (x.year, x.hour, x.minute)


# if you want to add diff. use timedelta

x + timedelta (hours = 1)

x + timedelta (days = 1)

x + timedelta (minutes = 20)

# to make the time more readable use strftime as per below
x.strftime('%m/%d/%Y %H:%M %p')



import calendar
import datetime
date = datetime.date(2021,5,16)
d = date.replace(day = calendar.monthrange(date.year, date.month)[1])
print(d)



