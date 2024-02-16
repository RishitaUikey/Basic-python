'''  Write a Python program to convert temperatures to and from Celsius and Fahrenheit.
[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
Expected Output :
60°C is 140 in Fahrenheit
45°F is 7 in Celsius '''

temp = float(input("Enter the temperature  = "))
unit = int(input("PRESS 1 to convert c to f and PRESS 2 to convert f to c = "))
c = temp 
f = c * (9/5) + 32
c = (5/9)*(f-32)

if (unit == 1):
    print(f"The temprature is converted from {c} to {f} ")
elif( unit == 2):
    print(f"The temprature is converted from {f} to {c} ")
else:
    print("Invalid option, Please enter 1 or 2 ")

