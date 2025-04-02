favorite_languages={
    "osman":"rust",
    "sadik":"python",
    "ali":"java",
    "ahmet":"javascript",

}
language=favorite_languages["osman"].title()
print(f"Osmanin favori dili {language}dir.")

#loop through the favorite_languages dictionary
for name,language in favorite_languages.items():
    print(f"\n{name.title()}in favori dili {language.title()}")

#Looping Through All the Keys in a Dictionary

for name in favorite_languages.keys():
    print(f"\n{name.title()}")

friends=["osman","sadik"]
for name in favorite_languages.keys():
    print(f"\nHi {name.title()}")
    if name in friends:
        language=favorite_languages[name].title()
        print(f"\t{name.title()}, bravo sen {language}'i seviyon demi kerata.")
if "Ali" not in favorite_languages.keys():
    print("Ali kardas nerdesin sen ya")

#sorted() function
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, tesekkurler pol pozisyonunda oldugun icin!!!")

print("Asagidaki diller secilmis:")
for language in favorite_languages.values():
    print(f"{language.title()}")

#To see each language chosen without repetition, we can use a set
print("Asagidaki diller secilmis:")
for language in set(favorite_languages.values()):
    print(f"{language.title()}")

favorite_languages={
    "ali":["rust","c"],
    "huseyin":["c","python"],
    "eylul":["rust"],
}

for name,languages in favorite_languages.items():
    print(f"\n{name.title()}'s favaori dili:")

    for languagea in languages:
        print(f"\t{languagea.title()}")