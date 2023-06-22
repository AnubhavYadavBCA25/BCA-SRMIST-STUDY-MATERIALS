print("Formulas of Circle!\n")

def area(x):
    return 3.14 * x * x

def circumference(x):
    return 2 * 3.14 * x

print("Choose your Operation:-")
print("1. Area of Circle")
print("2. Circumference of Circle")

while True:
    choice = input("Enter choice (1/2): ")
    
    if choice in ('1','2'):

        try:
            x = float(input("Enter the Radius: "))
        except ValueError:
            print("Invalid Input")
            continue

        if choice == '1':
            print("Area of Circle:",area(x))
        elif choice == '2':
            print("Circumference of Circle:",circumference(x))
        
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break
    else:
        print("Invalid Input")

print("Thank You For Using This :)") 


