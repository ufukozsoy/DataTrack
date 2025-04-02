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


