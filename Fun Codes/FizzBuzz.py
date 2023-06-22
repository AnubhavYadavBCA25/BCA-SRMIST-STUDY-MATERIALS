print('FizzBuzz Game :)\n')

def fizzbuzz(x):
    if x % 3 == 0 and x % 5 == 0:
        return "FizzBuzz"
    elif x % 3 == 0:
        return "Fizz"
    elif x % 5 == 0:
        return "Buzz"
    else:
        return x

while True:
    num = int(input("Enter the number:"))
    print(fizzbuzz(num))
    new_game = input("You want another game (yes/no):")
    if new_game == 'no':
        break
    else:
        print('Invalid Input!')

print("\nThank You For Playing") 

