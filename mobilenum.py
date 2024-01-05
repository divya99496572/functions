import re

st="67890112345ghjikl1234567890"
data=re.findall['\+91-[6789][0-9]{9}',st]
print(data)