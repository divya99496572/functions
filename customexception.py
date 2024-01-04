class DpInterrupt(Exception):
    pass
try:
    a=input('enter a string:- ')
    
    if a[0] in 'aeiouAEIOU':
        raise DpInterrupt('first char should not be a vowel')
except DpInterrupt:
    print('error handled')