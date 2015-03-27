import sys

try:
    f = open('file.py')
    s = f.readline();
    i = int(s.strip())
except IOError as e:
    print "I/O error({0}); {1}". format(e.errno, e.strerror)
except ValueError:
    print "Could not convert data to an integer."
except:
    print "Unexcepted error", sys.exc_info()[0]
    raise Exception('spam', 'eggs')
