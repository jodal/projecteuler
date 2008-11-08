from __future__ import division
import math
import re

def problem206(pattern):
    # XXX: Takes about 14 min to complete, but it works
    compiled = re.compile(r'^%s$' % pattern)
    min_value = 10 ** ((len(pattern) - 1) // 2)
    max_value = int(math.sqrt(2) * min_value)
    for i in xrange(min_value, max_value + 1, 2):
        squared = i ** 2
        if compiled.match(str(squared)) is not None:
            return i
        if i % 100000 == 0:
            print "%.2f%%" % ((i - min_value) * 100 / (max_value - min_value))

if __name__ == '__main__':
    print problem206('1.2.3.4.5.6.7.8.9.0')
