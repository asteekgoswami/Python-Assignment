from datetime import datetime
from time import strftime
dt=datetime.today()

# day month yearfull and 12 hout time format
# l1=dt.strftime("%d-%m-%Y and %I-%M-%p")
# print(l1)

# 12 hour format
# l1=strftime("%H-%M-%S")
# print(l1)

# print month in date
m=strftime('%d/%B/%Y')
print(m)