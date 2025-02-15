# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0

print(areas.index(20.0))
# Print out how often 9.50 appears in areas
print(areas.count(9.50))

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size
areas.append(24.5)
areas.append(15.45)


# Print out areas

print(areas)
# Reverse the orders of the elements in areas
areas.reverse()
# Print out areas
print(areas)

# Import the math package
import math

# Calculate C
C = 2 * 0.43 * math.pi

# Calculate A
A = math.pi * 0.43 ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))