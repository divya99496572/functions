import re
a='AP40AB1234asfgjjiklmAP30KP1234'
DATA=re.findall('AP[0-3]\d[A-Z]{2}\d{4}|AP40[A-Z]{2}\d{4}',a)
print(DATA)