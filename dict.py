my_dict = {}

my_dict = {1: 'watermelon', 2: 'guava'}

my_dict = {'name': 'Ariya', 1: [2, 3, 4]}

my_dict = {'name': 'Ariya', 'age': 11}

print(my_dict['name'])
print(my_dict.get('age'))

my_dict['age'] = 27
print(my_dict)

my_dict['address'] = 'Milky WAY'
print(my_dict)

my_dict.pop('age')
print(my_dict)

print("address:", my_dict['address'])

my_dict.clear()
print(my_dict)
