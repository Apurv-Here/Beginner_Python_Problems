# 4.	Write a program that will give you the sum of 3 digits

a = 123;
# sum will be 1+2+3 = 6

temp_sum = 0;

while a != 0:
    rem = a % 10;
    temp_sum = temp_sum + rem;
    a = a // 10;
    
print(temp_sum);