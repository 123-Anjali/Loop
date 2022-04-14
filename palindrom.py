num=int(input("enter the number"))
a=num
rev=0
while num>0:
    rev=rev*10+num%10
    num=num//10
if a==rev:
    print("palindrome",rev)
else:
    print("not palindrome",rev)

