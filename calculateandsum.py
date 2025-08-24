#Take an integer N as input. Your task is to calculate and print the sum of the digits of the given number N.
N = int(input("Enter a number "))
num = N
sum = 0
while num>0:
    sum += num%10
    num //=10
print("The sum of digit of",N,"is : ",sum)    

