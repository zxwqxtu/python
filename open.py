import sys 
import os

try:
    file = sys.argv[1] 
except Exception:
    file = raw_input('please enter file:')

while(not os.path.exists(file)):
    file = raw_input('please again enter file:')

for line in open(file, 'r'):
    if line[0] == '#':
        continue
    print line 
#xxxx
