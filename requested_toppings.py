available_toppings=["salam","sosis","zeytin","sucuk","peynir","biber"]
requested_toppings=["patates","sosis","zeytin"]

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"you are lucky, i am adding {requested_topping} to your pizza")
    else:
        print(f"we dont have {requested_topping}, sorry about that ")
print("\nFinished making your pizza!")