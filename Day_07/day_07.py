# creating set
# syntax
st = set()

# set with initial values
# syntax
st = {'item1', 'item2', 'item3', 'item4'}

# syntax
fruits = {'banana', 'orange', 'mango', 'lemon'}

# getting length of set
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
print(len(st))

fruits = {'banana', 'orange', 'mango', 'lemon'}
print(len(fruits))

# checking item in set
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
print("Does set st contain item3? ", 'item3' in st) # Does set st contain item3? True

fruits = {'banana', 'orange', 'mango', 'lemon'}
print('mango' in fruits ) # True

# adding item to set
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.add('item5')

fruits = {'banana', 'orange', 'mango', 'lemon'}
print(fruits)
fruits.add('lime')
print(fruits)

# adding multile items to set
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.update(['item5','item6','item7'])

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)
print(fruits)

# removing item from set
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item2')

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.remove('lemon')

# using pop() function to remove random item from set
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.pop()  # removes a random item from the set

# clearing items in a set
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.clear()

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear()
print(fruits) # set()

# converting list to set
# syntax
lst = ['item1', 'item2', 'item3', 'item4', 'item1']
st = set(lst)  # {'item2', 'item4', 'item1', 'item3'} - the order is random, because sets in general are unordered

fruits_list = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
print(fruits_list)
fruits = set(fruits_list) # {'mango', 'lemon', 'banana', 'orange'}
print(fruits)

# joining sets
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
print(fruits.union(vegetables)) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}

# deleting a set
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
del st

fruits = {'banana', 'orange', 'mango', 'lemon'}
del fruits
print(fruits) # prints Error : NameError: name 'fruits' is not defined
