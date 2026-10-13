import datetime

now = datetime.datetime.now()

print(now.year) #kuvab praeguse aasta (2026)
print(now.month) #kuvab praeguse kuu numbri (1-12)
print(now.day) #kuvab kuuvapäeva numbri (1-31)
print(now.hour) #kuvab tunni (0-23)

weekday = now.strftime("%A")
print(weekday)