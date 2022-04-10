import re


equation = '10 + 5'

print(re.search('(\d+) (\+) (\d+)', equation).groups())