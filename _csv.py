import csv
# with open('mca.csv','w',newline='') as csvfile:
#     data=csv.writer(csvfile)
#     data.writerow(['id','name','mobile','email'])
#     data1=[
#         [1,'divya',8996789123,'dp@gmail.com'],
#         [2,'ram',9444589123,'ram@gmail.com'],
#         [3,'ramya',9856712363,'rm@gmail.com'],
#     ]
#     data.writerows(data1)  


# with open('mca.csv','r') as csvfile:
#     data=csv.reader(csvfile)
#     for i in data:
#         print(i)

# with open('mca1.csv','w',newline='') as csvfile:
#     fieldnames=['id','name','mobile','email']
#     data=csv.DictWriter(csvfile,fieldnames)
#     data.writeheader()
#     rows=[
#         {'id':1,'name':'divya','mobile':8996789123,'email':'dp@gmail.com'},
#         {'name':'ram','id':2,'mobile':9444589123,'email':'ram@gmail.com'},
#     ]
#     data.writerows(rows)  


with open('mca1.csv','r') as csvfile:
    data=csv.DictReader(csvfile)
    for row in data:
        print(row['name'])
        
