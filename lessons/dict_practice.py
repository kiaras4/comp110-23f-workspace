"""practice with dictionaries - syntax."""

#Create a new dictionary
ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}
print("Create my dictionary")
print(ice_cream)

#Adding a key,value pair to the dictionary
ice_cream["mint"] = 3
print("Added mint to dictionary")
print(ice_cream)

#Removing a key, value pair from dictionary
ice_cream.pop("mint")
print("Removed mint")
print(ice_cream)

#Accessing value 
print(f"There are {ice_cream['chocolate']} orders of chocolate")

#Updating/modifying a value
ice_cream["vanilla"] = 10
# or
# ice_cream["vanilla"] += 2
print("After updating Vanilla:")
print(ice_cream)

# Print the length
print(f"There are {len(ice_cream)} pairs")

#Checking if values are in a dictionary
print("Chocolate in dictionary?")
print("chocolate" in ice_cream)
print("mint in dictionary?")
print("mint" in ice_cream)

#Using "in" in a conditional
if "mint" in ice_cream:
    print(ice_cream["mint"])
else:
    print("No orders of mint.")

#Loop through dictionary and print out each flavor and number of orders
for flavor in ice_cream:
    print(f"{flavor} has {ice_cream[flavor]} orders.")