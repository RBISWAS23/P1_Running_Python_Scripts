cities = ["Kolkata", "Delhi", "Murshidabad"]

# Print the original list and its type
print(cities)
print(type(cities))

# Access and print the element at index 2
print(cities[2])

# Append "Mumbai" to the list
cities.append("Mumbai")
print(cities)

# Insert "Purbasthali" at index 3
cities.insert(3, "Purbasthali")
print(cities)

#remove any eliments
cities.pop() # will remove last eliment from the arrey
print(cities)
cities.pop(1) # will remove number 1 eliment from arrey
print(cities)

# For Loop
for cit in cities:
    print("The current value is:")
    print(cit)

print("Process Completed")

#===============================================================================================================

Books=["Brief History of time", "Surveying and Levelling", "Hydrology", "Climatology"]
for book in Books:
    print(book)


print("Operation Completed😒")
