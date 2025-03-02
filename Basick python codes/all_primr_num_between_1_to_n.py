#A prime number is a positive integer that can only be divided by itself and 1 without leaving a remainder. For example, 2, 3, 5, 7, and 11 are all prime numbers. 

n= int(input("Enter a Number: "))
#n=1000
print("List of prime number between 1 to ",n )
for i in range(1,n+1):
    cn=i
    count=0
    for j in range(1,cn+1):
        if cn%j==0:
            count+=1
    if count==2:
        print(cn)