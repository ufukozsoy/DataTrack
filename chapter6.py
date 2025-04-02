#6-1. Person: Use a dictionary to store information about a person you know.
person={
    "first_name":"rumeysa",
    "last_name":"özsoy",
    "age":8,
    "city":"suhr",
    }
print(person["first_name"])
print(person["last_name"])
print(person["age"])
print(person["city"])
#6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
favourite_number={
    "harun":8,
    "rumeysa":3,
    "burak":4,
    "kenan":7,
    "omur":2
}
print(f'Burakin favori nosu:{favourite_number["burak"]}')
print(f'Hraunun favori nosu:{favourite_number["harun"]}')
print(f'{favourite_number["kenan"]}')
print(f'{favourite_number["omur"]}')
print(f'{favourite_number["rumeysa"]}')

#6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
glossary={
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs.",
}

word="string"
print(f"\n{word.title()}:{glossary[word]}")

word="comment"
print(f"\n{word.title()}:{glossary[word]}")

word="list"
print(f"\n{word.title()}:{glossary[word]}")

word="loop"
print(f"\n{word.title()}:{glossary[word]}")

word="dictionary"
print(f"\n{word.title()}:{glossary[word]}")

#Use a dictionary to store information about a person you know.
person={
    "first_name":"Rümeysa",
    "last_name":"Özsoy",
    "age":8,
    "country":"isvicre",
}
print(person["first_name"])
print(person["last_name"])
print(person["age"])
print(person["country"])

#Use a dictionary to store people’s favorite numbers
favourite_number={
    "Rümeysa":9,
    "Mehmet":3,
    "Ahmet":2,
    "Salih":1,
    "Ali":4
}
num=favourite_number["Rümeysa"]
print(f"Rümeysanin favori nosu {num} ")
num=favourite_number["Mehmet"]
print(f"Mehmetin favori nosu {num} ")
num=favourite_number["Ahmet"]
print(f"Ahmetin favori nosu {num} ")
num=favourite_number["Salih"]
print(f"Salihin favori nosu {num} ")
num=favourite_number["Ali"]
print(f"Alinin favori nosu {num} ")

#glossary
glossary = {
    "string": 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs.",
    'key': 'The first item in a key-value pair in a dictionary.',
    'value': 'An item associated with a key in a dictionary.',
    'conditional test': 'A comparison between two values.',
    'float': 'A numerical value with a decimal component.',
    'boolean expression': 'An expression that evaluates to True or False.',
    }



word="string"
print(f"\n{word.title()}:{glossary[word]}")
word="comment"
print(f"\n{word.title()}:{glossary[word]}")
word="list"
print(f"\n{word.title()}:{glossary[word]}")
word="loop"
print(f"\n{word.title()}:{glossary[word]}")
word="dictionary"
print(f"\n{word.title()}:{glossary[word]}")


#6.4
for name,definition in glossary.items():
    print(f"\n{name.title()}:{definition}")

#6.5
rivers={
    "nile":"egypt",
    "firat":"türkiye",
    "sas":"usa",

}

for river,country in rivers.items():
    print(f"\n{river.title()} runs through {country.title()}.")
print("\nAsagidakiler nehir isimlerimiz:")
for river in rivers.keys():
    print(f"{river.title()}")
print("\nAsagidakiler ulke isimlerimiz:")
for country in rivers.values():
    print(f"{country.title()}")

#6.6
favorite_languages={
    "osman":"rust",
    "sadik":"python",
    "ali":"java",
    "ahmet":"javascript",
}

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

print("\n")


friends=["osman","ali","rümeysa","mehmet"]
for friend in friends:
    if friend in favorite_languages.keys():
        print(f"Tesekkurler pola girdigin icin {friend.title()}")
    else:
        print(f"{friend.title()}, bekleriz pola gardas")


    


