import re
a="1 567 9 The 94 Date 52 is 04/01/2024"

data=re.findall('\d+',a)
print(data)