import datetime

#print (datetime.datetime.today())
#print (datetime.datetime.now())

d1 = datetime.datetime.today()
print(d1)

d1 = d1 + datetime.timedelta (days =10)
print(d1)

d2 = d1 + datetime.timedelta (days =5)
print(d2)

print (d1-d2)
print ((d1-d2).days)
print(d1.strftime( "%A  %d %B  %Y "))
