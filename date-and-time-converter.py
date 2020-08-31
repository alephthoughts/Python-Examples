from datetime import datetime
def date_time(time: str) -> str:
    #replace this for solution
    pdate = datetime.strptime(time,"%d.%m.%Y %H:%M")
    odate = datetime.strftime(pdate, "%-d %B %Y year %-H hours %-M minutes")
    if pdate.hour == 1:
        odate = odate.replace("hours", "hour")
    if pdate.minute == 1:
        odate = odate.replace("minutes", "minute")
    return  odate

if __name__ == '__main__':
    print("Example:")
    print(date_time('01.01.2000 00:00'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes", "Millenium"
    assert date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory"
    assert date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"