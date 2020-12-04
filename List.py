fruits = ["apple", "banana", "grape"]
print(fruits)

fruits.insert(1,2000)
fruits.insert(3,3000)
fruits.insert(5,5000)
fruits[5] = 1000
print(fruits)

fruits.remove(1000)
print(fruits)

fruits = [
        'apple', 2000, 
        'banana', 3000, 
        ['grape', ['mandarin', 'pear', 'lemon', 'tomato']]
         ]

print(fruits[4][1][2])

print(isinstance(fruits, list)) # isinstance(a, b) : Is a type b, true or false?
