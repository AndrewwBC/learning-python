# Key-Value

infos = {"name": "Andrew", "age": 25}

nested = {
    "id_0": {"name": "Campos", "age": 76},
    "id_1": {"name": "Andrew", "age": 25},
    "id_2": {"name": "Joseph", "age": 26},
    "id_3": {"name": "Toto", "age": 27}
}
print(nested.values())
# elements

for data in range(len(nested)):
    print(nested["id_"+str(data)])

# dict methods

# shallow copy 
infos.copy()
# get the value corresponding to the key
infos.get("name")
# returns all key/values 
infos.items()
# returns all keys
infos.keys()
# returns all values
infos.values()
# returns and delete the item corresponding to the key
infos.pop("name")
# returns and delete a random key/value
infos.popitem()
# remove all elements
infos.clear()

text = "abracadabra"
frequency = {}

for letter in text:
   if letter in frequency:
    frequency[letter] += 1
   else:
    frequency[letter] = 1
    
print(frequency)