def BMI_CAL(name,H_f,W_kg):
    bmi=round(W_kg/(H_f*0.3048)**2)
    print(name+" your  BMI is: ",bmi)
    if bmi < 25:
        return("you are thin")
    else:
        return("your are overweight")

x=str(input("Enter your name: "))
y=float(input("your height in feet: "))
z=float(input("your weight in kg: "))
print(BMI_CAL(x,y,z))
