requested_topping="mushroom"
if requested_topping!="ancor":
    print("Naber")

#testing multiple conditions

toppings=["salam","sosis","peynir"]

if "salam" in toppings:
    print("salam ekle")

if "zeytin" in toppings:
    print("zeytin ekle")

if "sosis" in toppings:
    print("sosis ekle")

print("\nPizza tamamdir.")

#if statement with for statement
toppings=['mushrooms', 'green peppers', 'extra cheese']

for topping in toppings:
    if topping=="green peppers":
        print("sorry we don't have green peppers")
    else:
        print(f"Adding {topping.title()} to the pizza")

print("this pizza is delicious")


#Checking That a List Is Not Empty
toppings=[]

if toppings:
    for topping in toppings:
        print(f"Added extra {topping} to your pizza")
    print("finished your pizza")
else:
    print("are you sure you want a plain pizza?")

