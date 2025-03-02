# a factorial is a function that multiplies a positive integer by every positive integer less than it, all the way down to 1. The symbol for factorial is an exclamation mark, like "!". For example, 7! means 1 × 2 × 3 × 4 × 5 × 6 × 7. 

fact = 1
n= int(input("Enter the no you want to factorial:  "))
for i in range(1,n+1):
    fact = fact*i

print("FACTORIAL OF ",n ,"is",fact)