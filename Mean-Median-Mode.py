import numpy as np
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

def mean(n):
    return np.mean(n)

def median(n):
    return np.median(n)

def mode(n):
    return stats.mode(n)

print("Select the Operation:\n")
print("1. Mean")
print("2. Median")
print("3. Mode")

while True:
    choice = input("Enter choice(1/2/3): ")

    if choice in ('1', '2', '3'):
        try:
            print("Enter the Data:")
            x = list(map(int, input("Enter: ").split()))
            print("List of Data:",x)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        if choice == '1':
            print("Mean of the Data:",mean(x))
        
        elif choice == '2':
            print("Median of the Data:",median(x))

        elif choice == '3':
            print("Mode of the Data:",mode(x))

        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break
    else:
        print("Invalid Input")