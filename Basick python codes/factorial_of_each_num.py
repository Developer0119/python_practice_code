#a factorial is a function that multiplies a number by every number below it till 1. For example, the factorial of 3 represents the multiplication of numbers 3, 2, 1, i.e. 3! = 3 × 2 × 1 and is equal to 6.

n= int(input("Enter the Number: "))
print("Factorial of a number between t to",n)
print("Number:Factorial")
for i in range(1,n+1):
    cn=i
    fact=1
    for j in range(1,cn+1):
        fact = fact*j
    print(cn,":",fact)