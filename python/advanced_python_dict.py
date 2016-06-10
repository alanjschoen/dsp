import re

### Question 1
print "\nQ1"

f_in = open('faculty.csv', 'r')
f_in.next()

faculty = dict()
for line in f_in:
    line = [w.strip() for w in line.split(',')]
    lastname = line[0].split()[-1]
    degree = line[1]
    title = re.match('.*Professor', line[2]).group()
    email = line[3]

    value = [degree, title, email]
    if lastname in faculty:
        faculty[lastname] += [value]
    else:
        faculty[lastname] = [value]
f_in.close()

for k in faculty.keys()[:4]:
    print "%s: %s  "%(k,faculty[k])

