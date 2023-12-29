a='ABCDEF'
b={j:i for i,j in enumerate(a) if i%2==0}
#b={a[i]:i for i in range(len(a)) if i%2==0}
print(b)