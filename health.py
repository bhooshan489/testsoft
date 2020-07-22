def BMI_CAL(name,H_f,W_kg):
    bmi=round(W_kg/(H_f*0.3048)**2)
    print(name.capitalize()+" your  BMI is",bmi,end=" and ")
    if bmi < 19:
        return("you are thin")
    elif 19<=bmi<=25:
        return("you are healthy")
    else:
        return("you are overweight")

x=str(input("Enter your name: "))
y=float(input("your height in feet: "))
z=float(input("your weight in kg: "))
print(BMI_CAL(x,y,z))
