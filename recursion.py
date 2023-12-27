#print all numbers of sum 1 to 10
def sum(st,ev):
    if st==ev:
        return st
    return st+ sum(st+1,ev)
out=sum(1,10)
print(out)
