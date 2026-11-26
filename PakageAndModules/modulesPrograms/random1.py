import random

print(random.random())
print(random.randint(1, 10))
print(random.choice([1,2,3,4,5,6,7,8,9,0,]))
numbers = [12, 21, 45, 78, 98, 55]

random.shuffle(numbers)

print(numbers)