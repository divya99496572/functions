def filter1(a):
    if 'a'<=a<='z':
        return True
    else:
        return False
def map1(a):
    
        return ord(a)
out=map(map1,(filter(filter1,'bcd@123aBC')))
#out=map(character,filter(character,"a1b2c3Def12@#9Z"))
print(list(out))

