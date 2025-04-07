

guest_list=["harun","mehmet","rumeysa"]


name=guest_list[0].title()
print(f"seni yarin yemege bekliyorum {name}")
name=guest_list[1].title()
print(f"seni yarin yemege bekliyorum {name}")
name=guest_list[2].title()
print(f"seni yarin yemege bekliyorum {name}")

print(f"maalesef {guest_list[0].title()} yemege gelemeyecek")

del guest_list[0]
guest_list.insert(0, 'ali')

name=guest_list[0].title()
print(f"seni yarin yemege bekliyorum {name}")
name=guest_list[1].title()
print(f"seni yarin yemege bekliyorum {name}")
name=guest_list[2].title()
print(f"seni yarin yemege bekliyorum {name}")

print(f"\nHey {guest_list[0].title()}, I found a bigger table, so I will call more people for the dinner ")
print(f"Hey {guest_list[1].title()}, I found a bigger table, so I will call more people for the dinner ")
print(f"Hey {guest_list[2].title()}, I found a bigger table, so I will call more people for the dinner ")

guest_list.insert(0,"ayhan")
guest_list.insert(2,"salih")
guest_list.append('elizabeth')
print(guest_list)

name=guest_list[0].title()
print(f"\nseni yarin yemege bekliyorum {name}")
name=guest_list[1].title()
print(f"seni yarin yemege bekliyorum {name}")
name=guest_list[2].title()
print(f"seni yarin yemege bekliyorum {name}")
name=guest_list[3].title()
print(f"seni yarin yemege bekliyorum {name}")
name=guest_list[4].title()
print(f"seni yarin yemege bekliyorum {name}")
name=guest_list[5].title()
print(f"seni yarin yemege bekliyorum {name}")


#shrinking the list
name=guest_list[5].title()
print(f"uzgunum yerim yok {name}")
popped_guest=guest_list.pop()


name=guest_list.pop()
print(f"uzgunum yerim yok {name}")


name=guest_list.pop()
print(f"uzgunum yerim yok {name}")


name=guest_list.pop()
print(f"uzgunum yerim yok {name}")

name = guest_list[0].title()
print(f"{name}, please come to dinner.")

name = guest_list[1].title()
print(f"{name}, please come to dinner.")

#empty the list
del(guest_list[0])
del(guest_list[0])

#prove the list is empy
print(guest_list)

# print(guest_list[0])
# print(guest_list[1])
# print(guest_list[2])
# print(guest_list[3])
# print(guest_list[4])
# print(guest_list[5])
# print(guest_list[6])
# print(guest_list[7])














