guests=['ahmet','faruk','riza']
print(f"Hi {guests[0].title()}, I would like to invite you dinner at 7 pm.")
print(f"Hi {guests[1].title()}, I would like to invite you dinner at 7 pm.")
print(f"Hi {guests[2].title()}, I would like to invite you dinner at 7 pm.")
print(f"Unfortunately {guests[0].title()} won't come to dinner.")
guests[0]='salih'
print(f"Hi {guests[0].title()}, I would like to invite you dinner at 7 pm.")
print(f"Hi {guests[1].title()}, I would like to invite you dinner at 7 pm.")
print(f"Hi {guests[2].title()}, I would like to invite you dinner at 7 pm.")

# We got a bigger table, so let's add some more people to the list.
print("\nWe got a bigger table!")
guests.insert(1,'emre')
guests.insert(2,'suat')
guests.append('mike')
print(guests)

name=guests[0].title()
print(f"please {name}, come to dinner")

name=guests[1].title()
print(f"please {name}, come to dinner")

name=guests[2].title()
print(f"please {name}, come to dinner")

name=guests[3].title()
print(f"please {name}, come to dinner")

name=guests[4].title()
print(f"please {name}, come to dinner")

name=guests[5].title()
print(f"please {name}, come to dinner")

# You can invite only two people for dinner.

print("You can invite only 2 people, because bigger table haven't arrived yet")

remove_guests=guests.pop(0)
print(f"I am sorry {remove_guests.title()}, I can't invite you dinner")

remove_guests=guests.pop(1)
print(f"I am sorry {remove_guests.title()}, I can't invite you dinner")

remove_guests=guests.pop(3)
print(f"I am sorry {remove_guests.title()}, I can't invite you dinner")

name=guests[0].title()
print(f"hi {name}, please come to the dinner")

name=guests[1].title()
print(f"hi {name}, please come to the dinner")

name=guests[2].title()
print(f"hi {name}, please come to the dinner")

del guests[0]
del guests[0]
del guests[0]
print(guests)
# print(guests[0])
# print(guests[1])
# print(guests[2])
# print(guests[3])





