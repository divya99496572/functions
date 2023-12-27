def fname(a):
        if type(a) in [int,float,complex,bool]:
            return True
        else:
            return False
           

out=filter(fname,[1,3+2j,False,2.5,{2,3},(2,3,5),{3:5},[2,4,5]])
print(list(out))