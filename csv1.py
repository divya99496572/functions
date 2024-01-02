import csv
with open('mca.csv','a') as csvfile:
    data=csv.writer(csvfile)
    data.writerow(['id','name','mobile','email'])
    data1=[
        [1,'divya',8996789123,'dp@gmail.com'],
        [2,'ram',9444589123,'ram@gmail.com'],
        [3,'ramya',9856712363,'rm@gmail.com'],
    ]
    data.writerows(data1)  

