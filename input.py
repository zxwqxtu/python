'''
while True:
    reply = raw_input('Enter text:')
    if reply == 'stop': 
        break
    print(reply)
else:
    print('x','x')
x = 'SPAM'
if 'rubbery' in 'shrubbery':
    print(x*8)
    x += 'NI'
    if x.endswith('NI'):
        x *= 2
        print(x)

a = 2 or 3
b = 2 and 3
print(a, b)
'''

a = [1, 2, 3]
b = [2, 3, 4]
for v in zip(a,b):
    print(v[0])
    
