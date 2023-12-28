a=["abcd",{1:2},[4,5,6],{4,7},(9,8,7)]
def length(a):
    if type(a) in [list,tuple,str,dict]:
        return len(a)
    else:
        return a
a=[len(i) for i in a]
print(a)