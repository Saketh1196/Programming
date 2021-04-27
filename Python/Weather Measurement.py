Temp=float(input("Enter the temperature in Fahrenheit: "))
Celsius=(5/9)*(Temp-32)
print("The temperature in Celsius is: ",Celsius)
while True:
    if Celsius>30:
        print("The Weather is too hot. Please take care")
    elif Celsius<10:
        print("The Weather is too Cold. Wear Warm Clothes")
    else:
        print("Standard Weather")
    break
