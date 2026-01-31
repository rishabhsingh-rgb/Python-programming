def months_days(year,month):
    days=[31,28,31,30,31,30,31,31,30,31,30,31]

    if leap_year(year) and month==2:
        return 29
    else:
        return days[month-1]

def leap_year(year):
    if ((year%4==0 and year%100!=0)or(year%400==0)):
        return True
    else:
        return False

months=["January","February","March","April","May","June","July","August","September","October","November","December"]

year=int(input('Enter the year: '))
month=int(input('Enter the month: '))
print(f"There are {months_days(year,month)} days in {months[month-1]}, {year}.")