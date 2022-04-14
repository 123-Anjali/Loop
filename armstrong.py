a=int(input("enter the number::"))
i=a
sum=0
while i>0:
    sum=sum+(i%10)*(i%10)*(i%10)
    i=i//10
if a==sum:
    print("armstrong number")
else:
    print("not armstrong number")


