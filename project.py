print("Welcome to Book My Show")
name=(input('please enter a name:- '))
seats=int(input('please enter the number of seats,you want to book:-'))
category=int(input('please select  1.Diamond \n 2.Gold \n 3.silver :- '))
if category == 1:
    amount=seats*200
elif category == 2:
    amount=seats*150
elif category == 3:
    amount=seats*100
print(f'hi {name} you have booked {seats}seats and total amount is {amount}')


 
