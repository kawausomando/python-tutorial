import re

print(re.findall(r'\bf[a-z]*', 'whitch foot or hand fell fastest'))

# ['foot', 'fell', 'fastest']

print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat'))