from datetime import datetime, timedelta
def roundTime(dt=None, roundTo=1):
   if dt == None : dt = datetime.now()
   seconds = (dt.replace(tzinfo=None) - dt.min).seconds
   rounding = (seconds+roundTo/2) // roundTo * roundTo
   return dt + timedelta(0,rounding-seconds,-dt.microsecond)


now=datetime.utcnow()
rounded=roundTime(now)
print(rounded)
print(now)
print(type(now));