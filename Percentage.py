# Step1: Take input of all the subjects.
# We will take three subjects.

comp_sci = float(input("Enter marks of the Computer Science:"))
maths = float(input("Enter marks of the Maths:"))
science = float(input("Enter marks of the Science:"))

# Step2: Calculate the percentage.
# Marks in all subjects is out of 100.
percent = (comp_sci + maths + science)*100/300

# Step3: Set the conditions for conditional statements.

if percent > 60:
    print("Congratulations! You Pass with 1st division.")

elif percent <= 60 and percent > 50:
    print("Congratulations! You Pass with 2nd division.")

elif percent <= 50 and percent > 40:
    print("Congratulations! You Pass with 3rd division.")

elif percent <= 40 and percent >= 33:
    print("Congratulations! You Pass.")

else:
    print("Bad Luck! You failed.")

# In this program we used conditional statements more time. So, we understand that we will used conditional (elif) many times in our programs.