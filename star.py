rows=int(input('no of rows:- '))
columns=int(input('no of cols:- '))
for i in range(rows):
    for j in range(columns):
       if i==0 or i==rows-1:
            if j==0 or j==columns-1:
               print("@",end=' ')
            else:
                print("*",end=' ')
       else:
            
          if  j==i or rows-i-1==j :
            print('@ ',end=' ')
          else:
           print("*",end=' ')
    print()