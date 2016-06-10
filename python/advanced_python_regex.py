import pandas as pd
import numpy as np

# Read CSV
df = pd.read_csv('faculty.csv', sep=',', skipinitialspace=True)

# Get list of all degrees
degrees_raw = [d for l in df['degree'].values for d in l.split()]

# Convert to lower case and remove periods for matching
degrees_low = [d.lower().replace('.', '') for d in degrees_raw]

# Get unique degrees
degrees_unique = set(degrees_low)

print "Number of unique degrees: %d"%(len(degrees_unique))

# Process each unique degree
for d in degrees_unique:

    # Find all matching degrees in their original format
    matches = [dr for (dl,dr) in zip(degrees_low, degrees_raw) if dl==d]

    # Find the most frequent format of this degree
    d_fmt = max(set(matches), key=matches.count)

    # Print degree with the count
    print '%s: %d'%(d_fmt,len(matches))