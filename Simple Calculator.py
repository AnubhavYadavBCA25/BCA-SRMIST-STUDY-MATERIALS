print('Welcome To The Simple Calculator!\n')

def add(x,y):
    return x+y

def substract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

def exp(x,y):
    return x**y

print('Select Operation:')
print('1. Addition')
print('2. Substarction')
print('3. Multiplication')
print('4. Division')
print('5. Exponentiation')

while True:
    choice = input('Enter Choice(1/2/3/4/5): ')

    if choice in ('1','2','3','4','5'):
        try:
            num1 = float(input('Enter First Number: '))
            num2 = float(input('Enter Second Number: '))
        except ValueError:
            print('Invalid Input. Please Enter A Number.')
            continue

        if choice == '1':
            print(num1,'+',num2,'=',add(num1,num2))

        elif choice == '2':
            print(num1,'-',num2,'=',substract(num1,num2))

        elif choice == '3':
            print(num1,'*',num2,'=',multiply(num1,num2))

        elif choice == '4':
            print(num1,'/',num2,'=',divide(num1,num2))

        elif choice == '5':
            print(num1,'**',num2,'=',exp(num1,num2))

        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == 'no':
            break
    else:
        print('Invalid Input')

print("\nThank You For Using Me :)")