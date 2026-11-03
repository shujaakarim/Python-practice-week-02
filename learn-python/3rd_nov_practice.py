# data types
# mutable
# List, dictonary, set

# immutable:
# int, tuples, string, float, double, bool

# Example1
"""
customer = "noor foods"
customer.upper()
print(customer)

customer = customer.upper()
print(customer)
print(type(customer))
"""

# Practice: strings can't change

"""
coat = "7856o"
# coat[4] = 0
coat = coat.replace("o", "0")
print(coat)
"""

"""
# Example 2: lists can change
prices = [850, 1200, 400]
prices.append(3100)
prices[0] = 900
print(prices)
"""

"""
cart = ["rice", "oil"]
cart.append("sugar")
# print(cart)

cart[1] = "ghee"
# print(cart)

cart.remove("rice")
print(cart)
"""

"""
prices = [850, 1200, 400]
for i in range(len(prices)):
    prices[i] = round(prices[i] * 1.1)
print(prices)
"""

"""
updated_price = []
prices = [850, 1200, 400]
print(len(prices))
for price in prices:
    updated_price.append(price)
    price = round(price * 1.1)
    print(updated_price)
"""

"""
# Example 3: watching identity with id()
stock = 120
print(id(stock))
stock += 30
print(id(stock))


prices = [850, 1200]
print(id(prices))
prices.append(400)
print(id(prices))
"""


todays_orders = [4500, 12800]
report_orders = todays_orders.copy()
report_orders.append(2300)
print(todays_orders)
print(report_orders)
