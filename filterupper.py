def upper(a):
    if  'A'<=a<='Z':
        return True
    else:
        return False
out=filter(upper,'aBc@1567DEfgh')
print(list(out))