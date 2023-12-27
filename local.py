a=10
def outer():
    b=20
    def inner():
        nonlocal b
        c=30 
        b=100
        print(b)#100-2
        print(c)#30-3
    print(b)#20-1
    inner()
    print(b)#100-4
outer()


    