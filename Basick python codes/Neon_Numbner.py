#A neon number is a number where the sum of the digits of its square is equal to the original number. It's also known as a pseudoperfect number. 

num = int(input("Enter the Number: "))

sq= num*num
sum = 0
while(sq>0):
    sum = sum+sq%10
    sq = sq//10

if(sum==num):
    print(num,"is a Neon Number")
else:
    print(sum,"is Not Neon Number")