# 1.	User will input (3ages).Find the oldest one

age1 = int(input(" Enter the age1 = "));
age2 = int(input(" Enter the age2 = "));
age3 = int(input(" Enter the age3 = "));

max_age = max(age1, age2, age3);
print("The max age is: ", max_age);