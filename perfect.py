a=int(input("enter the number"))
sum=0
i=1
while (i<a):
    if a%i==0:
        sum=sum+i
    i=i+1
if sum==a:
    print("perfect number",a) 
else:
    print("not perfect number")      
