signals=input('enter the traffic signal:- ')
match signals:
    case 'red':
       print('stop')
    case 'yellow':
        print('ready to go')
    case 'green':
        print('go')
    case _:
        print(None)