#What are odd and even numbers with examples? Odd numbers are those numbers that cannot be divided into two equal parts, whereas even numbers are those numbers that can be divided into two equal parts. Examples of odd numbers are 3, 5, 7, 9, 11, 13, 15,… Examples of even numbers are 2, 4, 6, 8, 10, 12, 14,…

num = int(input("Enter the Number: "))
n=num%2
if n==0:
    print(n,"it's number is even")

else:
    print(n,"it's number is odd")