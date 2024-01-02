#file=open('mca.txt','w')
#data='welcome to the mca department'
#file.write(data)
#file.close()

#file=open('mca.txt','a')
#data=[ 'divya\n','abhi\n','krish\n','assu\n']
#file.writelines(data)
#file.close()


file=open('mca.txt','r')
data=file.read()
print(data)
file.close()

