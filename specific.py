try:
    #a=2+'2'
    a=dict('34')
    print(a)
except TypeError:
    print('error handled')
except ValueError:
    print('can not type cast string to dict')
finally:
    print('exception handled')

def sum(a,b):
    return a+b
print(sum(2,3))