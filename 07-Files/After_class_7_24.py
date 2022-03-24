import re
m = "To be, or not to be, that is the question"
vow = re.findall("[aeiouy]",m)
n=0
for i in vow:
    n+=1
print("The number of vowels:", n)