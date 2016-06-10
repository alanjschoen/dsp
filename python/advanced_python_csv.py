import re

# Open file as plain text
text = open("faculty.csv","r").read()

# Find all emails
emails = re.finditer("([\w.]*@[\w.]*)", text)

file_out = open('emails.csv', 'w')
for e in emails:
    file_out.write("%s\n"%e.group())
file_out.close()