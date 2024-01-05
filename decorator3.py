def cal(func):
    def inner():
        print('operation started')
        func()
        print('operation done')
    return inner
@cal
def add():
    a=int(input('enter a:-'))
    b=int(input('enter b:-'))
    print(a+b)
add()