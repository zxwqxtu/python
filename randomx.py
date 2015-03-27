import random

#random.seed(2)
a = random.randint(1, 3)
print a
print random.randint(1, 3)
print random.randrange(1, 10, 2)
print random.choice([1, 2, 3])
x = [1, 3, 4]
random.shuffle(x)
print x
print(random.random())
xx = set(x)
xx.add(5)
xx.pop()
print xx
#print(a)
