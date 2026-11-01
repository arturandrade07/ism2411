

# Exercise 1
from copy import error


print("\nExercise 1\n")
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

# Exercise 2
print("\nExercise 2\n")
print(inventory[0])
print(inventory[-1])
middle = len(inventory) // 2
print(inventory[middle])

# Exercise 3
print("\nExercise 3\n")
print(inventory[0:3])
print(inventory[-2:])
print(inventory[::2])

# Exercise 4
print("\nExercise 4\n")
inventory.append("envelope")
print(inventory)
inventory.remove("tape")
print(inventory)
inventory.sort()
print(inventory)

# Exercise 5
print("\nExercise 5\n")
coords = (40.7128, -74.0060)
try:
    coords [0] = 99
except TypeError as error:
    print("Type error caught:", error)
    print("Tuples can't be modified. Since locations coordinates cannot change as well, tuples are used to represent immutable locations.")
print(coords)

# Exercise 6
print("\nExercise 6\n")
sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count
print(f"Total: {total}")
print(f"Count: {count}")
print(f"Average: {average}")
print(f"Best: {max(sales)}")
print(f"Worst: {min(sales)}")

# Exercise 7
print("\nExercise 7\n")
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []
for price in prices:
    discounted.append(round(price * 0.9, 2))
print(f"Original prices: {prices}")
print(f"Discounted prices: {discounted}")

# Exercise 8 
print("\nExercise 8\n")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []
for sale in sales:
    if sale > 300: 
        high_sales.append(sale)
print(f"High sales: {high_sales}")
print(f"Count: {len(high_sales)}")
print(f"Average: {round(sum(high_sales) / len(high_sales), 2)}")