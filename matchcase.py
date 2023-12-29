seats=int(input('enter a seats:- '))
option=int(input('enter option here:- '))
match option:
    case 1:
        print("Diamond class")
        amount=seats*200
    case 2:
        print("Golden class")
        amount=seats*150
    case 3:
        print("Silver class")
        amount=seats*100
    case _:
        print('invalid option')
        amount=None 

print(amount)
