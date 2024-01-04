import re
a='ABCDD1234EdfryehABCDk1234GnjkdnLJMNO0876D'
data=re.findall('[A-Z]{5}\d{4}[A-Z]',a)
print(data)