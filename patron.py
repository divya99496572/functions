rows=int(input('enter no of rows:- '))
out='''
'''
for i in range(1,rows+1):
    out=out+(' '*(rows-i)+'* '*i)
    out=out+'\n'
for i in range(0,rows):
    out=out+(' '*(rows-i)+'*'*(i*2+1))
    out=out+'\n'
name=input('enter name of the file:- ')
with open(f'{name}.txt','w')as file:
    file.write(out)
