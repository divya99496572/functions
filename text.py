import re 
with open("C:\\Users\\administrator.MCA\\Desktop\\content.txt",'r')as file:
    
    data=file.read()
    out=re.findall('[aA][a-z]*',data)
    print(len(out))