def calculate_bmi(height, weight):
    bmi = weight / (height ** 2)
    return bmi


def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi >= 18.5 and bmi < 25:
        return "Normal weight"
    else:
        return "Overweight. Watch your figure."


while True:
    try:
        height = float(input("Enter your height in centimeters: "))
        weight = float(input("Enter your weight in kilograms: "))

        bmi = calculate_bmi(height, weight)
        category = get_bmi_category(bmi)

        print("Your Body Mass Index (BMI) is: {:.2f}".format(bmi))
        print("BMI Category: ", category)

        choice = input("Do you want to calculate BMI again? Enter 'off' to stop or enter to continue: ")
        if choice.lower() == 'off':
            break
    except ValueError:
        print("Please enter valid height and weight values.")

print("Program stopped.")

