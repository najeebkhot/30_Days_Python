# conditionals

# if condition
# syntax
'''if condition:
    this part of code runs for truthy conditions
'''

a = 3
if a > 0:
    print('A is a positive number')
# A is a positive number
    
# if-else statement
# syntax
"""    
if condition:
    this part of code runs for truthy conditions
else:
     this part of code runs for false conditions
"""

a = 3
if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')

# if-elif-else statement
# syntax
"""
if condition:
    code
elif condition:
    code
else:
    code
"""
a = 0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')

# short hand
# syntax
''' code if condition else code '''

a = 3
print('A is positive') if a > 0 else print('A is negative') # first condition met, 'A is positive' will be printed

# nested condition
"""
# syntax
if condition:
    code
    if condition:
    code
"""

a = 0
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')

# if condition and logical operator
"""
# syntax
if condition and condition:
    code
"""

a = 0
if a > 0 and a % 2 == 0:
        print('A is an even and positive integer')
elif a > 0 and a % 2 !=  0:
     print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')


# if condition or logical operator
"""
# syntax
if condition or condition:
    code
"""

user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
        print('Access granted!')
else:
    print('Access denied!')
