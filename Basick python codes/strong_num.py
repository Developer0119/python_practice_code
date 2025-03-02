#A number is called strong number if sum of the factorial of its digit is equal to number itself. For example: 145. since. 1! + 4!

num= int(input("Enter the number: "))
t=num
sum=0
while(num):
    i=1
    p=1
    r=num%10
    while(i<=r):
        p=p*i
        i+=1
    sum=sum+p
    num=num//10

if(sum==t):
    print(t,"is a Strong number")

else:
    print(t,"is not a Strong number")