import datetime
today = datetime.date.today()
print(type(today))
print(today)

d1 = today.strftime('Dzisiaj jest %d dzień i %m miesiaca')
print(d1)
d2 = today.strftime('%d--%m--%y')
print(d2)

now = datetime.datetime.now()
print(type(now))
print(now)

my_now = now.strftime('%M-%m-%S')
print(my_now)