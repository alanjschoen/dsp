import pandas as pd
import numpy as np
import re

# Read CSV
df = pd.read_csv('faculty.csv', sep=',', skipinitialspace=True)
print df.columns

### Question 1
print "\nQ1"

# Get list of all degrees
degrees_raw = [d for l in df['degree'].values for d in l.split()]

# Convert to lower case and remove periods for matching
degrees_low = [d.lower().replace('.', '') for d in degrees_raw]

# Filter out invalid degrees
degrees_low = [d for d in degrees_low if d.isalpha()]

# Get unique degrees
degrees_unique = set(degrees_low)
print "Number of unique degrees: %d"%(len(degrees_unique))
print ">> Degree | Count"
print "--- | ---"

# Process each unique degree
for d in degrees_unique:

    # Find all matching degrees in their original format
    matches = [dr for (dl,dr) in zip(degrees_low, degrees_raw) if dl==d]

    # Find the most frequent format of this degree
    d_fmt = max(set(matches), key=matches.count)

    # Print degree with the count
    print '%-7s | %d'%(d_fmt,len(matches))

### Question 2
print "\nQ2"

# Get titles (everything up to 'professor')
titles = df['title'].str.extract('(.*Professor)').values.tolist()

# Get unique titles
titles_unique = set(titles)
print "Number of unique titles: %d"%(len(titles_unique))
print ">> Title | Count"
print "--- | ---"

for t in titles_unique:
    print '%-20s | %d'%(t,titles.count(t))

### Question 3
print "\nQ3"

# Open file as plain text
text = open("faculty.csv","r").read()

# Find all emails
emails = re.findall("([\w.]*@[\w.]*)", text)
print ">> " + str(emails) + "  "

### Question 4
print "\nQ4"

# Get domains by splitting emails on @
domains = [e.split('@')[1] for e in emails]

# Get unique domains
domains_unique = list(set(domains))

print "Number of unique domains: %d"%(len(domains_unique))
for d in domains_unique: print(">> %s  "%d)
