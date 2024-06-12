def get_valid_input(prompt, input_type, max_attempts=3):
    attempts = 0
    while attempts < max_attempts:
        user_input = input(prompt).strip()
        try:
            validated_input = input_type(user_input)
            return validated_input
        except ValueError:
            attempts += 1
            if attempts < max_attempts:
                print("Invalid input. Please try again.")
    return "Maximum number of attempts reached. Exiting..."

def BMR_CAL(name, gender, age, height, weight):
    if gender.upper() == 'M':
        BMR = round((13.397 * weight) + (4.799 * height) - (5.677 * age) + 88.362)
        return f"{name}, your ideal BMR is {BMR} Calories/day"
    elif gender.upper() == 'F':
        BMR = ((9.247 * weight) + (3.098 * height) - (4.330 * age) + 447.593)
        return f"{name}, your ideal BMR is {BMR} Calories/day"
    else:
        return "Enter correct gender (M/F)"

name = get_valid_input("Enter your name: ", str.capitalize)
gender = get_valid_input("Enter your gender (M/F): ", str.upper)
while gender not in ('M', 'F'):
    gender = get_valid_input("Invalid input. Please enter 'M' for male or 'F' for female: ", str.upper)
if gender == "Maximum number of attempts reached. Exiting...":
    print(gender)
    exit()
age = get_valid_input("Enter your age: ", int)
if age == "Maximum number of attempts reached. Exiting...":
    print(age)
    exit()
while age <= 0:
    age = get_valid_input("Invalid input. Age must be a positive integer: ", int)
height = get_valid_input("Your height in cm: ", float)
if height == "Maximum number of attempts reached. Exiting...":
    print(height)
    exit()
while height <= 0:
    height = get_valid_input("Invalid input. Height must be a positive number: ", float)
weight = get_valid_input("Your weight in kg: ", float)
if weight == "Maximum number of attempts reached. Exiting...":
    print(weight)
    exit()
while weight <= 0:
    weight = get_valid_input("Invalid input. Weight must be a positive number: ", float)

print(BMR_CAL(name, gender, age, height, weight))
