import datetime as dt
format = '%y-%m-%dT%H:%M:%S'
t1 = dt.datetime.strptime('2008-10-12T14:45:52',format)
print('Day'+ str(t1.day))
print('Moth'+ str(t1.month))
print('Minute'+ str(t1.minute))
print('Scond',+str(t1.second))

t2= dt.datetime.now()
diff = t2-t1
print('How many days difference?'+ str(diff.days))