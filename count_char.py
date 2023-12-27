
def count_char(a,ch):
    count=0
    for i in a:
        if i==ch:
         count+=1
    return count
count=count_char("happy new year",'p')
print(count)