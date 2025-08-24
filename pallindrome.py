# You are given an integer A as input, and you need to determine whether it is a palindrome or not.
A = int(input("Enter a number "))
if str(A) == str(A)[::-1]:
    print("It is pallindrome")
else:
    print("Not a pallindrome")    
