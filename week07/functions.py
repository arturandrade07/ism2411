# Midterm: Loops, Conditionals, and Functions. 1 page of hand written notes on one side. 
# Artur Andrade
# Self-assessment
# 1. First bug I spotted was line 11 missing a colon at the end, from explaining the code to the duck because it sounded
# inconsistent with I had just seen in line 80 of this file. 
# 2. apply_discount(price, tier) gathers the price, assigns it to a tier, applying the discount based on that tier and 
# returns the final price. I believe a colleague could use it because it is pretty much straightforward code. However,
# I don't think they would be able to build up the code.
# 3. AI used only as a tool to understand debug as suggested in class. 

# Exercise 1
# Defining a function
print("\n Exercise 1")
def calculate_tax(price, rate):
    return price * rate

# Calling the function

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax for $100 at 7%: ${tax1:.2f}")
print(f"Tax for $250 at 8%: ${tax2:.2f}")
print(f"Tax for $350 at 5%: ${calculate_tax(350, 0.05):.2f}")

# Exercise 2
print("\n Exercise 2")
def apply_discount(price, tier):
    if tier == 'gold':
        return price * 0.85
    elif tier == 'silver':
        return price * 0.90
    elif tier == 'bronze':
        return price * 0.95
    else:
        return price

# Calling the function with different tiers
original_price = 200

for tier in ['gold', 'silver', 'bronze', 'none']:
    print(f"{tier}: ${apply_discount(original_price, tier):.2f}")

#Exercise 3
print("\n Exercise 3")

def final_price(price, tax_rate, discount_tier):
    discounted_price = apply_discount(price, discount_tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax

#Calling the final price
print(f"final_price(200, 0.07, 'gold'): ${final_price(200, 0.07, 'gold'):.2f}")

#Exercise 4

orders= [(200, 'gold'), (150, 'silver'), (80, 'bronze'), (500, 'none')]

rate=0.07
for price, tier in orders:
    total = final_price(price,rate,tier)
    print(f"Price: ${price:.2f}, Tier: {tier}, Total: ${total:.2f}")


# Exercise 6
print("\n Exercise 6")

x=100 #global x

def double_it():
    x=999 # local x
    return x * 2

print(x)
print(double_it())
print(x)


# Exercise 5 : broken_sales.py
# broken_sales.py - trace and diagnose before fixing anything.
print("\n Exercise 5")
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale
# Bug: replaced total as each sale went through. Not added. "+=" instead to add as sales come in. 
print(f"Total: ${total}")

count = 0
for sale in sales:
    # Bug: line 11 was missing the colon at the end. 
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales):
#Bug: a 5 item list has indexes from 0-4, so when 5 is reached, it falls out of range. 
    print(sales[i])
    i += 1