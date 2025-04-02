#4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.
for number in range(1,21):
    print(number)

#4-4. One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers. 
#(If the output is taking too long, stop it by pressing CTRL-C or by closing the output window.)


#4-5. Summing a Million: Make a list of the numbers from one to one million, and then use min() and max() to make sure
# your list actually starts at one and ends at one million. Also, use the sum() function to see how quickly Python 
#can add a million numbers.

numbers=list(range(1,1000001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

#4-6. Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. 
#Use a for loop to print each number.

for value in range(1,20,2):
    print(value)

odd_numbers = list(range(1, 20, 2))

for number in odd_numbers:
    print(number)
#4-7. Threes: Make a list of the multiples of 3, from 3 to 30. Use a for loop to print the numbers in your list.

threes=list(range(3,31,3))
for number in threes:
    print(number)

#4-8. Cubes: A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python. 
#Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a 
#for loop to print out the value of each cube.

qubes=[]
for value in range(1,11):
    qubes.append(value**3)
print(qubes)

#4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.

qubes=[number**3 for number in range(1,11)]
for qube in qubes:
    print(qube)

# (4-10. Slices: Using one of the programs you wrote in this chapter, 
# add several lines to the end of the program that do the following:

#Print the message The first three items in the list are:. 
# Then use a slice to print the first three items from that program’s list.
#Print the message Three items from the middle of the list are:. 
# Then use a slice to print three items from the middle of the list.
#Print the message The last three items in the list are:. Then use a slice to print the last three items in the list.)

items=["araba","ev","hali","motor","at","esek"]
print("First 3 items on the list are:")
print(items[:3])
print("\nThree items from the middle of the list are:")
print(items[2:5])
print("\nLast 3 items on the list are:")
print(items[-3:])


myfavorite_pizzas = ['pepperoni', 'hawaiian', 'veggie']
friend_pizzas=myfavorite_pizzas[:]
myfavorite_pizzas.append("elmali")
friend_pizzas.append("armutlu")


print("\nMy favourite pizzas are:")
for pizza in myfavorite_pizzas:
    print(f"-{pizza}")
print("\nMy friend's favouite pizzas are:")
for pizza in friend_pizzas:
    print(f"-{pizza}")

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("\nMy favourite foods are:")
for food in my_foods:
    print(f"-{food}")
print("\nMy friend's favouite foods are:")
for food in friend_foods:
    print(f"-{food}")

#4.13 buffet
print("\n")
print("This is the old list:")
buffet_food=("ekmek","su","zeytin","peynir","bal")
for food in buffet_food:
    print(food)

print("\n")
print("This is the updated list:")
updated_buffet_food=("armut","elma","zeytin","peynir","bal")
for food in updated_buffet_food:
    print(food)





