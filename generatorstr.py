def sample(a):
   for i in range (0,len(a)):
       if a[i] in 'aeiouAEIOU':
           yield a[i]
           yield i
out=sample("God father anil")
res=''
for i in out:
    res+=str(i)
#print(list(out))
print(res)