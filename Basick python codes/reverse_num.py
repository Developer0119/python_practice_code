#A reverse number is a number that has had its digits rearranged in reverse order. For example, the reverse of 1234 is 4321. 

n= int(input("Enter a number:\t"))
num=n
rev=0
while(n!=0):
    rev=rev*10
    rev=rev+n%10
    n=n//10

print(num,"it's reverse number is",rev)