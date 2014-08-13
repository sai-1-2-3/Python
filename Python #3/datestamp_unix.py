from datetime import datetime
from time import mktime


date = 'It\'s Monday, September 2nd 2013'

unixTime = datetime.strptime(date, 'It\'s %A, %B %dnd %Y')
converted = mktime(unixTime.timetuple())
print (converted)
    
