car="subaru"
if car=="subaru":
    print("afferim")

#5.3

alien_color="green"
if alien_color=="green":
    print("you have just earned 5 points")

alien_color="white"
if alien_color=="green":
    print("you have just earned 10 points")

#5.4

alien_color="blue"

if alien_color=="white":
    print("bravo")

else:
    print("no bravo")

#5.5

alien_color="blue"

if alien_color=="green":
    print("5 points")
elif alien_color=="red":
    print("10 points")
else:
    print("20 points")
#5.6 stage of life

age=400

if age<2:
    print("you are a baby")
elif age<4:
    print("you are a toddler")
elif age<13:
    print("you are a child")
elif age<20:
    print("you are a teenager")
elif age<65:
    print("you are a adult")
else:
    print("you are old")

#5.7 favourite fruits

fruits=["kavun","muz","nar","hurma"]
if "kavun" in fruits:
    print("oley i have a kavun.")
if "muz" in fruits:
    print("oley i have a muz.")
if "nar" in fruits:
    print("oley i have a nar.")
if "elma" in fruits:
    print("oley i have a elma.")
if "hurma" in fruits:
    print("oley i have a hurma.")

#5.8, 5.9 hello admin
usernames=[]

if usernames:
    for username in usernames:
        if username=="admin":
            print("Hello admin, would like to see report")
        else:
            print(f"Hello {username}, hosgeldin safalar getirdin.")
else:
    print("We need to find some users.")

#5.10
current_users=["ali","ozgur","luka","rumeysa","mehmet"]
new_users=["rumeysa","mehmet","harun","firat","omur"]

for new_user in new_users:
    if new_user in current_users:
        print(f"{new_user}, Lutfen baska bir username al.")
    else:
        print(f"{new_user}, bu username i alabilirsin.")

#5.11
numbers=[1,2,3,4,5,6,7,8,9]
for number in numbers:
    if number==1:
        print("1st")
    elif number==2:
        print("2nd")
    elif number==3:
        print("3rd")
    else:
        print(f"{number}th")    
