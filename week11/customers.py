#1. I would use .get() when a key might be missing, maybe an email or phone numbers. It gives 
# you a default value instead of throwing an error. I would use [] when I know the key is there, like a name or tier.
#2. It is similar to using a SUMIF in excel to add totals based on a condition. Python is desired for larger datasets
# because it is faster and more efficient than excel. It is also easier to automate and integrate with other systems.

print ("\n Exercise 1 \n")

customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 8750,
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])

print(customer)

print ("\n Exercise 2 \n")
customer ['phone'] = '555-5555'
print(customer)
customer['tier'] = 'platinum'
print(customer)
del customer ['email']
print(customer)

print(customer.get('ytd_spend', 0))


print("\n Exercise 3 \n")
print(customer.get("email", "no email on file"))

try:
    print(customer["email"])
except KeyError:
    print("KeyError: 'email' is not in the dictionary")


print("\n Exercise 4 \n")
for key, value in customer.items():
    print(f"{key}: {value}")

# .items() gives the key and the value together on each loop.
# Looping over the dict without .items() gives only the keys,
# so you have to use customer[something] to get each value.
for something in customer:
    print(something, customer[something])

print("\n Exercise 5 \n")
tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.1,
    "platinum": 0.15
}

purchase = 200
discount_rate = tier_discounts.get(customer["tier"], 0)
final_price = purchase * (1 - discount_rate)
print(f"Tier: {customer['tier']}")
print(f"Discount Rate: {discount_rate * 100:.2f}%")
print(f"Final Price: ${final_price:.2f}")

print("\n Exercise 6 \n")
customers = [
    {"name": "Bob", "tier": "silver", "ytd_spend": 3200},
    {"name": "Alice", "tier": "gold", "ytd_spend": 8750},
    {"name":  "David", "tier": "bronze", "ytd_spend": 450},
]

for record in customers:
    print(record)

for record in customers:
    discount = 300 * tier_discounts.get(record["tier"], 0)
    print(f"{record['name']} - {record['tier']} - discount on $300: ${discount:.2f}")

print("\n Exercise 7 \n")
catalog = {
    "Widget A": {"price": 9.99, "stock":150},
    "Gadget C": {"price": 49.99, "stock": 8},
}

for name, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {name} - only {details['stock']} left")


print("\n Exercise 8 \n")
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
]

sales_by_region = {}
for sale in transactions:
    region = sale["region"]
    amount = sale["amount"]
    sales_by_region[region] = sales_by_region.get(region, 0) + amount

print(sales_by_region)

for region in sorted(sales_by_region): print(f"{region}: ${sales_by_region[region]:.2f}")