import datetime

today = datetime.date.today()

wkday = 2 # wednesday

end_date = datetime.date(2012, 11, 22) # 22 nov 2012

# finding the next ordinal for scheduled activity
def find_next(wkday, start_date, end_date):
    today_o = today.toordinal()
    today_wkday = today.weekday()
    end_o = end_date.toordinal()
    if wkday < today_wkday:
        wkday_diff = today_wkday - wkday 
        start_date_o = today_o + 7 - wkday_diff
    else:
        wkday_diff = wkday - today_wkday
        start_date_o = today_o + wkday_diff
    while 1:
        yield datetime.date.fromordinal(start_date_o)
        start_date_o += 7
        if start_date_o > end_o:
            break

# finding the next ordinal for scheduled activity
def find_next(wkday, start_date, end_date):
    today_wkday = today.weekday()
    if wkday < today_wkday:
        diff = datetime.timedelta(7 - today_wkday + wkday)
    else:
        diff = datetime.timedelta(wkday - today_wkday)
    start_date = today + diff
    while 1:
        yield start_date
        start_date += datetime.timedelta(7)
        if start_date > end_date:
            break

for next_day in find_next(wkday, today, end_date):
    print next_day


