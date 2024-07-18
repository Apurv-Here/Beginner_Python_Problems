# 3.	User will input (2numbers).Write a program to swap the numbers

# Swapping using Bitwise XOR: ^
print("Swapping using Bitwise XOR: ^");
a = 5;
b = 10;

print(f"Before swapping value of a is {a} and value of b is {b} ");

a = a ^ b;
b = a ^ b;
a = a ^ b;

print(f"Before swapping value of a is {a} and value of b is {b} ");



print();

num1 = int(input("Enter the first number: "));
num2 = int(input("Enter the second number: "));
print(f"Before swapping numbers are {num1} and {num2} ");

# Swapping using third variable
print("Swapping using third variable");
temp = num1;
num1 = num2;
num2 = temp;

print(f"Before swapping numbers are {num1} and {num2} ");
