#def add(a,b,c=2,d=0,e=0):
   #  return a+b+c+d+e
# out=add(3,5,6,5,3)
#print(out)

#def add(*args):
 #   out=0
#for i in args:
 #     out+=i
    #return out
#res=add(2,6,7,8,9)
#print(res)

#def add(a,b=0,*args,**kwargs):
#    print(a,args)
#    print(kwargs)
#add(3,5,9,k=87)

def add(a,b,c):
    print(a)
    print(b)
    print(c)
add(*{'b':3,'c':5,'a':89})
add(**{'b':3,'c':5,'a':89})
    

