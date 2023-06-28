cities = ['Kathmandu', "Kathmandu", 'Pokhara',
          'Butwal', 'Birgunj']  # Aka lists in python
data = ['Kathmandu', True, 12, [12, "More"]]  # Aka lists in python

print(data[3][1])
data.append("New data")
print(data)

data.pop(2)   # Remove the last element and returns the popped value
print(data)
