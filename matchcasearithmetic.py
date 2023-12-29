num1=int(input('enter a number:- '))
num2=int(input('enter a number:- '))
operator=int(input('enter a operator:-'))
match operator:
    case 1:
        print('addition')
        num=num1+num2
    case 2:
        print('subtraction')
        num=num1-num2
    case 3:
        print('multiplication')
        num=num1*num2
    case 4:
        print('power')
        num=num1**num2
    case 5:
        print('modulus div')
        num=num1%num2
    case 6:
        print('true div')
        num=num1/num2
    case 7:
        print('floor div')
        num=num1//num2
    case _:
        print('invalid operator')
        num=None
print(num)