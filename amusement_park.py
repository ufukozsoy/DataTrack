#if-elif-else
age=12
if age<4:
    print("ucretsiz girebilirsin")
elif age<12:
    print("25 frank ode")
else:
    print("40 frank ode")

#if elif else
age=4
if age<4:
    price=0
elif age<12:
    price=25
else:
    price=40

print(f"Your admission price is {price}")

#adding another elif

age=69
if age<4:
    price=0
elif age<12:
    price=25
elif age<65:
    price=40
else:
    price=10

print(f"Your admission price is {price}")

#without else statement

age=69
if age<4:
    price=0
elif age<12:
    price=25
elif age<65:
    price=40
elif age>=65:
    price=10

print(f"Your admission price is {price}")

