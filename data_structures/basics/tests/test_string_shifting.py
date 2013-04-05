"""
Test set for shift
Created: 5 April 2013
"""

import nose
from nose.tools import eq_, ok_
from data_structures.basics.string_shifting import shift

def test_basic():
    eq_(shift("abc", 1), "bca")
    eq_(shift("abcd", 1), "bcda")
    eq_(shift("abcdef", 3), "defabc")
    eq_(shift("abcdefg", 4), "efgabcd")
    
    eq_(len(shift("abc", 1)), len("cab"))
    
def run():
    nose.run()
    
if __name__ == '__main__':
    run()
