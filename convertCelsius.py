# program takes input from user
# user enters temperature in Celsius
# program converts user input into Fahrenheit


celsius = float(input("Please enter temperature in Celsius: "))
fahrenheitFormula = (celsius * 9/5) + 32 
print('%.2f Celsius is: %0.2f Fahrenheit' %(celsius, fahrenheitFormula))