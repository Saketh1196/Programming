weight=float(input("Enter your Weight in Kilograms: "))
Height=float(input("Enter your Height in Metres: "))
BMI= weight/(Height*Height)
print("Your Body Mass Index is: ", BMI)
while(BMI>0):
    if BMI<18.5:
        print("You are underweight. Eat more to gain Weight")
    elif (BMI>18.5 and BMI<24.9):
        print("You are Healthy")
    elif(BMI>25 and BMI<29.9):
        print("You are Overweight. Please Start Dieting")
    else:
        print("You are Obese. Too bad for health!!!")
    break

             
