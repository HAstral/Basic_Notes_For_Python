import datetime

date=datetime.date(2024,2,3)
today=datetime.date.today()
time=datetime.time(12,45,30)
now=datetime.datetime.now()

now = now.strftime("%H:%M:%S %m-%d-%Y")
target_datetime=datetime.datetime(2030,1,3,12,45,33)
current_datetime=datetime.datetime.now()
if target_datetime<current_datetime:
    print("The Target Date has passed.")
else:
    print("The Target Date has not passed yet.")
# print(now) 