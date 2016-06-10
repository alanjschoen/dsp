import re

### Question 6
print "\nQ6"

# Open CSV
f_in = open('faculty.csv', 'r')

# Skip first line
f_in.next()

faculty = dict()
for line in f_in:

    # Split line into fields
    line = [w.strip() for w in line.split(',')]

    # Extract info
    lastname = line[0].split()[-1]
    degree = line[1]
    title = re.match('.*Professor', line[2]).group()
    email = line[3]

    # Add data to dictionary
    value = [degree, title, email]
    if lastname in faculty:
        faculty[lastname] += [value]
    else:
        faculty[lastname] = [value]

# Close file
f_in.close()

# Print first 3 entries
for k in faculty.keys()[:3]:
    print "`%s: %s`  "%(k,faculty[k])

### Question 7
print "\nQ7"

# Open CSV
f_in = open('faculty.csv', 'r')

# Skip first line
f_in.next()

faculty = dict()
for line in f_in:

    # Split line into fields
    line = [w.strip() for w in line.split(',')]

    # Get first name and last name
    ind = line[0].rfind(' ')
    lastname = line[0][ind+1:]
    firstname = line[0][:ind]

    # Get degree
    degree = line[1]
    # degree = re.sub('Ph\.?D\.?', 'Ph.D.', degree, flags=re.IGNORECASE)
    # degree = re.sub('Sc\.?D\.?', 'Sc.D.', degree, flags=re.IGNORECASE)

    # Get title
    title = re.match('.*Professor', line[2]).group()
    email = line[3]

    # Add entry to dictionary
    key = (firstname, lastname)
    value = [degree, title, email]
    faculty[key] = value

# Close file
f_in.close()

# Print first 3 entries
for k in faculty.keys()[:3]:
    print "`%s: %s`  "%(k,faculty[k])

### Question 8
print "\nQ8"

# Sort keys by last name
keys_sorted = sorted(faculty.keys(), key=lambda k: k[1])

# Print all key/value pairs
for k in keys_sorted:
    print "`%s: %s`  "%(k,faculty[k])