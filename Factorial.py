#Step 1: Taking input from user.
num = int(input("Enter your number:"))

#Step 2: Define the initial factorial value.
factorial = 1

#Step 3: Set all the possible conditions.
if num == 1 or num == 0:
    print("Factorial of 1 and 0 is 1.")

elif num < 0:
    print("Sorry! Factorial of less than 0 doesn't exists.")

else:
#Step 4: Set the range of the number (i) in factorial (num+1 is not included).
    for i in range(1,num+1):

#Step 5: Calculating the factorial.
        factorial = factorial*i
    print("Factorial of",num,"is",factorial)

#Note: To understand the concept of factorial program in python, you have to learn the concept of factorial in mathematices.
#Note: Learn the concept of 'conditional statement' (if,elif,else) and 'for' loop from "w3school Python Tutorial" for better understanding.