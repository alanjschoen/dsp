from datetime import datetime
# https://docs.python.org/2/library/datetime.html#strftime-strptime-behavior

pf = "%m/%d/%y"

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'

pattern = "%m-%d-%Y"
d1 = datetime.strptime(date_start, pattern)
d2 = datetime.strptime(date_stop, pattern)
print "%d days from %s to %s"%((d2-d1).days, d1.strftime(pf), d2.strftime(pf))

####b)  
date_start = '12312013'  
date_stop = '05282015'

pattern = "%m%d%Y"
d1 = datetime.strptime(date_start, pattern)
d2 = datetime.strptime(date_stop, pattern)
print "%d days from %s to %s"%((d2-d1).days, d1.strftime(pf), d2.strftime(pf))

####c)  
date_start = '15-Jan-1994' 
date_stop = '14-Jul-2015'

pattern = "%d-%b-%Y"
d1 = datetime.strptime(date_start, pattern)
d2 = datetime.strptime(date_stop, pattern)
print "%d days from %s to %s"%((d2-d1).days, d1.strftime(pf), d2.strftime(pf))