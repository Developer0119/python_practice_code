#An automorphic number is a number whose square ends with the same digits as the number itself. For example, 52 = 25, so 5 is an automorphic number. 

n = int(input("Enter the Number: "))
num = n
sq = n*n
t = 10
equel =  False
print("Square of" ,n,"is",sq)
while(n>0):
    r=sq%t
    if(num==r):
        equel=True
        break
    n=n//10
    t=t*10

if(equel):
    print(num,"is an Automorphic Number")
else:
    print(num,"is Not an Automorphic Number")