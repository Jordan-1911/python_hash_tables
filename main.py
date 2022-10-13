# The following illustrates variuos data types in Python 3 and accessing items

import array as arr

# Dictionary
big_tech_addresses = {
    "Meta": "1 Hacker Way, Menlo Park, CA 94025",  # two strings are acceptable as type
    "Google": "1600 Ampitheater Parkway, Mountain View, CA, 94043",
    "Apple": "1 Infinite Loop, Cupertino, CA 95014"
}  # the values can be of any data type (int, String, boolean, list)
print()
print(big_tech_addresses["Apple"])
print()


# Potential dictionary indexing problems
# Let us check if a key exists in a dictionary, and if so, the value of its pair will print
print(big_tech_addresses["Meta"])


# However, if the ket is not present, an exception will be thrown
# print(big_tech_addresses["Amazon"])
# this will output: "KeyError" 'Amazon'
# this can be worked around by first using the following
print()  
print(big_tech_addresses.keys())


# how to check if key exists in dictionary with "in"
print()
if "Meta" in big_tech_addresses:
    print("The element is present in the dictionary")
else:
    print("No luck")

print()
if "Amazon" in big_tech_addresses:
    print("The element is present in the dictionary")
else:
    print("No luck")
 

# List
my_list = ["Meta", "Google", "Apple"]
print()
print(my_list[2])

# Array
my_arr = arr.array('i', [1, 2, 3])
print()
for i in my_arr:
    print(i)

