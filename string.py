x = int(raw_input("enter interge:"));
print x
s = """
bafdsfsfsfsdskk
"""
print (s*3).split('s')
print s.encode('gbk')

for x in s*3:
    print x

[x * 2 for x in s]
print map(ord, x)
print x

print "aba" 'xx' "badk"+'nnn'
print ('kk','vv')

print(r'c:\new\text.dat')
print('1'*4)

s = 'spam'
S = 'S'+s[1:]
s1 = s.replace('s', 'S')
print (S==s1)

print("%s" %"wq")
print("%s:%s" %("name","wq"))
print("%(key)s:%(value)s" %{'key':"name", 'value':"wq"})
print('{0},{1}'.format('span', 'ham'))
print('{key},{0}'.format('wq', key='name'))
