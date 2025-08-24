#Take an integer A as input. You have to print the sum of all odd numbers in the range [1, A]. 
A = int(input("Enter a number "))
total = 0
for i in range(1, A+1, 2):
    total += i
print("The sum of all odd numbers between 1 and",A,"is : ",total)    
