#helloword.py
from ClassOne import ClassOne 
myBuddy = ClassOne()
myBuddy.add(222)
print(myBuddy.getCurrent())

print("hello world,python");
'''
def helpme():
    print 'help yourself'

helpme()
'''

a = 0;
b = 2;
print(a+b)

a = 20; b=20
if a >= 22:
    print('if')
elif a >= 21:
    print('elif')
else:
    print('else')


def fun(b):
    print(b)

fun(b) 

for a in range(2, 3):
    print(a)
print(type("aba"+"kkk"))

myExample = {'someItem':2, 'otherItem':3}
print(myExample['otherItem'])

for a in myExample:
    print(a, myExample[a])


myList = [1,2,3]
myList.append(4);
print(myList)

myTuple = (1, 2, 3)
print(myTuple)

str = "abacdfsfsfsfsd"
print("%.20s\t%.10s" %(str, str))

