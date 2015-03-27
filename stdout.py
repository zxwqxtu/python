import sys

print(sys.argv)

print 'Dive in'
saveout = sys.stdout
fsock = open('out.log', 'w')
sys.stdout = fsock
print 'This message will be logged'
sys.stdout = saveout
fsock.close()
