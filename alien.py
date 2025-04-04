alien_0={"color":"green","points":5}
print(alien_0['color'])
print(alien_0['points'])

#received points
alien_0={"color":"green","points":5}
new_points=alien_0["points"]
print(f"You have just earned {new_points} new points.")

#add two new pieces of information 
alien_0={"color":"green","points":5}
print(alien_0)

alien_0["x_coordinates"]=0
alien_0["y_coordinates"]=25
print(alien_0)

#Starting with an Empty Dictionary
alien_0={}
alien_0["color"]="green"
alien_0["points"]=5
print(alien_0)

#Modifying Values in a Dictionary
alien_0={"color":"green"}
print(f"alien color is {alien_0['color']}")
alien_0={"color":"yellow"}
print(f"alien color is now {alien_0['color']}")

#track the position of an alien that can move at different speeds
alien_0={"x_position":0,"y_position":25,"speed":"medium"}
print(f"Original position:{alien_0['x_position']}")
# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0["speed"]=="slow":
    x_increment=1
elif alien_0["speed"]=="medium":
    x_increment=2
else:
    x_increment=3
#alien new position
alien_0["x_position"]=alien_0["x_position"]+x_increment

print(f"New position of alien is:{alien_0['x_position']}")

#Removing Key-Value Pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0["points"]
print(alien_0)

#A Dictionary of Similar Objects
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
# Make a list of the aliens
aliens = [alien_0, alien_1, alien_2]
# Show the color of the first alien
print(aliens[0]['color'])
# Show the color of the second alien
print(aliens[1]['color'])
# Show the color of the third alien
print(aliens[2]['color'])
# Make an empty list for storing aliens
aliens = []
# Create 30 aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
# Show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
# Show how many aliens have been created
print(f"Total number of aliens: {len(aliens)}")
# Making a List in a Dictionary
# Store information about a pizza being ordered
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
# Summarize the order
print(f"You ordered a {pizza['crust']}-crust pizza"
      f" with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)
# Nesting
# A list of dictionaries
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
# Make a list of the aliens
aliens = [alien_0, alien_1, alien_2]
# Show the color of the first alien
print(aliens[0]['color'])
# Show the color of the second alien
print(aliens[1]['color'])
# Show the color of the third alien
print(aliens[2]['color'])
# A list in a dictionary
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
# Summarize the order
print(f"You ordered a {pizza['crust']}-crust pizza"
      f" with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)

# A dictionary in a dictionary
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
# Build a dictionary of user information
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

# Build a dictionary of user information
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
# Store additional information about the user
user_0['location'] = 'chicago'
user_0['age'] = 39
# Display the user's information
print(f"Username: {user_0['username']}")
print(f"Full name: {user_0['first']} {user_0['last']}")
print(f"Location: {user_0['location']}")