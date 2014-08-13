import datetime
import time

var = time.time()

print(datetime.datetime.fromtimestamp(var).strftime('%Y-%m-%d %H:%M:%S'))
print(datetime.datetime.fromtimestamp(var).strftime('It\'s %A, %B %d %Y %H:%M:%S'))
