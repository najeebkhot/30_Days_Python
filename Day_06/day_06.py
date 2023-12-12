# creating tuple
# syntax
empty_tuple = ()
# or using the tuple constructor
empty_tuple = tuple()

# tuple with initial values
# syntax
tpl = ('item1', 'item2','item3')

fruits = ('banana', 'orange', 'mango', 'lemon')
print(fruits)

# length of tuple
# syntax
tpl = ('item1', 'item2', 'item3')
len(tpl)

print(len(fruits))

# accessing values in tuple
# Syntax
tpl = ('item1', 'item2', 'item3')
first_item = tpl[0]
second_item = tpl[1]

fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[0]
second_fruit = fruits[1]
last_index =len(fruits) - 1
last_fruit = fruits[last_index]

print("last fruit : ",last_fruit)

# accessing values from the last
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
first_item = tpl[-4]
second_item = tpl[-3]

fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[-4]
second_fruit = fruits[-3]
last_fruit = fruits[-1]

print("last fruit : ",last_fruit)

# slicing tuple
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
all_items = tpl[0:4]         # all items
all_items = tpl[0:]         # all items
middle_two_items = tpl[1:3]  # does not include item at index 3

fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[0:4]    # all items
all_fruits= fruits[0:]      # all items
orange_mango = fruits[1:3]  # doesn't include item at index 3
orange_to_the_rest = fruits[1:]

# range of negative indexes
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
all_items = tpl[-4:]         # all items
middle_two_items = tpl[-3:-1]  # does not include item at index 3 (-1)

fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[-4:]    # all items
orange_mango = fruits[-3:-1]  # doesn't include item at index 3
orange_to_the_rest = fruits[-3:]

# changing tuple to list
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
lst = list(tpl)

fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple'
print("tuple to list : ",fruits)     # ['apple', 'orange', 'mango', 'lemon']
fruits = tuple(fruits)
print("list to tuple : ",fruits)     # ('apple', 'orange', 'mango', 'lemon')

# checking an item of tuple
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
'item2' in tpl # True
print('item2' in tpl) # True

# joining tuple
# syntax
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5','item6')
tpl3 = tpl1 + tpl2

fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)

# deleting tuple
# syntax
tpl1 = ('item1', 'item2', 'item3')
del tpl1

fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits
print(fruits) # Error : NameError: name 'fruits' is not defined

