#slicing a list
players=["ahmet","salih","ergun","okan","rumeysa"]
print(players[0:3])
print(players[1:4])
print(players[:3])
print(players[2:])
print(players[-3:])
#Looping Through a Slice
players=["ahmet","salih","ergun","okan","rumeysa"]
print("here are the players on my team:")
for player in players[0:3]:
    print(player.title())

#Copying a List
players=["ahmet","salih","ergun","okan","rumeysa"]
print("here are the players on my team:")
for player in players[:]:
    print(player.title())
#The original list is unchanged
print("The original list is unchanged:")
print(players)
#Removing all instances of a value from a list
#Removing all instances of a value from a list
players=["ahmet","salih","ergun","okan","rumeysa"]
