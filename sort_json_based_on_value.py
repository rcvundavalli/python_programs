# Array of JSON Objects
products = [{"name": "HDD", "brand": "Samsung", "price": "$100"},
            {"name": "Monitor", "brand": "Dell", "price": "$120"},
            {"name": "Mouse", "brand": "Logitech", "price": "$10"}]

# Print the original data
print("The original JSON data:\n{0}".format(products))
# Sort the JSON data based on the value of the brand key
products.sort(key=lambda x: x["brand"])

# Print the sorted JSON data
print("The sorted JSON data based on the value of the brand:\n{0}".format(products))


"""
# import pprint module
import pprint

# Array of JSON Objects
employee_list = [
{
    'name': 'firoz shah',
    'post': 'HR',
    'email': 'Accountant'
},
{
    'name': 'Aiyan hasan',
    'post': 'Sales',
    'email': 'Manager'
},
{
    'name': 'Mahmuda Feroz',
    'post': 'Marketing',
    'email': 'CEO'
}]

# Print the original JSON list
print("Array of JSON objects before sorting:")
pprint.pprint(employee_list)

# Declare function to return the sorted data based on name
def sort_by_key(list):
    return list['name']

# Print the sorted JSON list based on the name key
print("\nArray of JSON objects after sorting:")
pprint.pprint(sorted(employee_list, key=sort_by_key))
"""
