a='ABC'
b=[4,5,6]
out={}
#for i in range(len(a)):
 #   out+=a[i]+b[i]
for i,j in zip(a,b):
    out[i]=j
print(out)
       