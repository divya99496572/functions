def odd(a):
    if a %2 != 0:

        return a**2

out=map(odd,filter(odd,range(1,100)))
print(list(out))