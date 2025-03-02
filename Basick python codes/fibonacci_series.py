# a series of numbers in which each number ( Fibonacci number ) is the sum of the two preceding numbers. The simplest is the series 1, 1, 2, 3, 5, 8, etc.
a=0
b=1
n=int(input("Enter n for how many time generate  series: "))
#n=51
print("FIBONACCI SERIES")
print(" ",a," ",b,end="")
for i in range(n):
    c= a+b
    a=b
    b=c
print(" ",c,end=" ")