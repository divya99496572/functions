a=10
b=20
def sample():
    global a
    a=30
    print(a)#30-2
    print(b)#20-3
print(a)#10-1
sample()
print(a)#30-4