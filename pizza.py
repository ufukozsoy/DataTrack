#pizzas=['kasarli','sucuklu','peynirli']
#for pizza in pizzas:
#	print(f"I like {pizza.title()} pizza")
#print("I really like eating sucuklu pizza")

pizzalar=["kasarli","sucuklu", "mantarli"]

for pizza in pizzalar:
    print(pizza)


for pizza in pizzalar:
    print(f"bugunku {pizza} pizza cok guzeldi.")
    
print("pizzayi gercekten cok sevirem.")

# Store information about a pizza being ordered.

pizza={
    "crust":"thick",
    "toppings":["mushroom","extra cheese"]
}
# Summarize the order.
print(f"You have ordred a {pizza['crust']} crust with the following toppings:")

for topping in pizza["toppings"]:
    print(f"{topping}")

# A dictionary in a dictionary
user_0={
    "username":"efermi",
    "first":"enrico",
    "last":"fermi"
}

user_0["location"]="chicago"
user_0["age"]=39
# Display the user's information
print(f"Username: {user_0['username']}")
print(f"Full name: {user_0['first']} {user_0['last']}")
print(f"Location: {user_0['location']}")