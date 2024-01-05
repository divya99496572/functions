import re
a='divyaprasanna158@gmail.com 123@gmail.com'
data=re.findall('[a-zA-Z]+[a-zA-Z0-9]*\@gmail\.com',a)
print(data)