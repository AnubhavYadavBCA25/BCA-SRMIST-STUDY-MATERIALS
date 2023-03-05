# Table by 'for' loop

# Step 1: Take input from the user.
num = int(input("Enter the number whose table you want:"))

print("Here is the table of",num)

# Step 2: Using 'for' loop to print the table.
for i in range(1,11):  # 'i' is the integer value in range 1 to 11 (11 is not included)

# Step 3: Taking a variable and make the table of given number by multiplying 'num' and 'i'. 
    table = num*i
    print(num,"x",i,"=",table)

#---------------------------------------- Second Method --------------------------------------------#

# Another method for making table by 'while' loop.
num = int(input("Enter your number whose table you want:"))

print("Here is the table of",num)

i = 1  # Define the initial value of 'i'

while i<11:  # Setting the limit of 'i' by while loop
    
    table = num*i  

    print(num,"x",i,"=",table)

    i += 1  # Adding 1 number after every multiple until it will reach to 10.

# Note: Both codes are provide same output. So, it's depends on you which codes you understand clear.