import calendar

c = calendar.Calendar()

yeardays = c.yeardayscalendar(2012, 1)

def show(mn, dow):
    daysoftheweek = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
    monthsoftheyear = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 
                       'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    for m,month in enumerate(yeardays):
        for week in month[0]:
            for day,date in enumerate(week):
                if m==mn and date and day==dow:
                    print "%s the %s of %s" % (daysoftheweek[day],
                                               date,
                                               monthsoftheyear[m])

show(0, 3)

            


