"""Day2011"""
def dayin2011(day, month):
    """show weekday in 2011 by date and month"""
    days_total = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    weekdays = ['Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday']
    day += days_total[month-1]
    weekday = day%7
    print(weekdays[weekday])
dayin2011(int(input()), int(input()))
