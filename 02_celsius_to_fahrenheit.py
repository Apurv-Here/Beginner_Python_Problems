# 2. Write a program that will convert celsius value to fahrenheit

cel_temp = int(input("Enter the temperature in celsius: "));

# Formula for celsius to fahrenheit is = (9/5)*C + 32

fahr_temp = ((9/5) * cel_temp) + 32 ;
fahr_temp = round(fahr_temp)

print(fahr_temp);