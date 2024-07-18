# 5.	Write a program that will reverse a four digit number.Also it checks whether the reverse is true.

a = 1211;
temp_a = a;

b = 0;

while temp_a != 0:
    rem = temp_a % 10;
    b = b*10 + rem;
    temp_a = temp_a // 10;

print("The value of a is: " , a);
print("The value of reverse of a is: " , b);


if a == b:
    print("Reverse is true");
else:
    print("Reverse is false");