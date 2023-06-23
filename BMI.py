print("Welcome to BMI Calculator!")

def bmi_calculator(weight,height):
    bmi = weight/(height*height)
    return bmi

while True:
    weight_in_kg = float(input("Enter your weight in kg:"))
    height_in_meter = float(input("Enter your height in meters:"))
    bmi = bmi_calculator(weight_in_kg, height_in_meter)
    
    if bmi <= 18.5:
        print("Your BMI is",bmi,"and your BMI status is underweight.")
    
    elif bmi > 18.5 and bmi <= 24.9:
        print("Your BMI is",bmi,"and your BMI status is normal.")

    elif bmi > 24.9 and bmi <= 29.9:
        print("Your BMI is",bmi,"and your BMI status is overweight.")

    elif bmi > 29.9 and bmi <= 34.9:
        print("Your BMI is",bmi,"and your BMI status is obesity mild (class 1).")

    elif bmi > 34.9 and bmi <= 39.9:
        print("Your BMI is",bmi,"and your BMI status is obesity moderate (class 2).")

    elif bmi > 40:
        print("Your BMI is",bmi,"and your BMI status is obesity morbid (class 3).")
    
    else:
        pass

    next_calculation = input("Do you want another calculation (yes/no)?:")
    if next_calculation == 'no':
        break
    
print("Thank You For Using This BMI Calculator :)")