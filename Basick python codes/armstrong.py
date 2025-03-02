#An Armstrong number is a number that is equal to the sum of its own digits, each raised to the power of the number of digits. For example, 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153. 
n = int(input("Enter the Number: "))
t = n
r = 0
while(n>0):
    a = n%10
    r = r +a*a*a
    n  = n // 10

if(r==t):
    print("Armstrong Number")

else:
    print("Not An Armstrong Number")

