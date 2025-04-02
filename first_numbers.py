#using range function
for value in range(1,5):
    print(value)

numbers=list(range(1,5))
print(numbers)

#even numbers

even_numbers=list(range(2,10,2))
print(even_numbers)

#square
squares=[]
for value in range(1,7):
    square=value**2
    squares.append(square)
    
print(squares)

#omit square
squares=[]
for value in range(1,7):
    squares.append(value**2)
print(squares)

#Simple Statistics with a List of Numbers
digits=[1,4,7,9]
print(min(digits))
print(max(digits))
print(sum(digits))

#squares.py
squares=[value**2 for value in range(1,10)]
print(squares)