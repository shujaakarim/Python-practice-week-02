# 1. Unique cities. Using ["Karachi", "Lahore", "Karachi", "Multan", "Lahore"],
# print how many different cities there are (expected: 3) and then the cities in alphabetical order.

"""
Unique_cities = ["Karachi", "Lahore", "Karachi", "Multan", "Lahore"]
print(len(Unique_cities))
unique_cities_count = set(Unique_cities)
print(len(unique_cities_count))
print(sorted(unique_cities_count))
"""

"""
#QUESTION 02
order_ids = ["A101", "A102", "A101", "A103", "A102"]
seen = set()
for i in order_ids:
    if i in seen:
        print(f"repeated order {i}")
    else:
        seen.add(i)
"""


"""
# question 03
# 3. Customers we lost. Using the two sets below, print which customers stopped ordering,
# which are new and which stayed, each as a sorted list:
last_month = {"Noor Foods", "Bilal Traders", "Zara Textiles"}
this_month = {"Noor Foods", "Karachi Crafts"}
print(f"{last_month - this_month} stopped ordering")
"""

names = ["Khan", "Laiba", "Shahzaib", "mustansir"]
names.sort()
print(names)
names.reverse()
print(names)
