import datetime

date=datetime.date(2024,2,3)
today=datetime.date.today()
time=datetime.time(12,45,30)
now=datetime.datetime.now()

now = now.strftime("%H:%M:%S")

print(now)