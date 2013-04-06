"""
Test set for StringChecker
"""
import nose
from nose.tools import eq_, ok_
from data_structures.basics.first_occurrence import StringChecker, NOT_FOUND

def test_not_found():
    checker = StringChecker()
    
    eq_(checker.first_occurrence("ABCDE", "aBCDE"), NOT_FOUND)
    eq_(checker.first_occurrence("ABCDE", "FGHIJ"), NOT_FOUND)
    eq_(checker.first_occurrence("ABCDE", "ABCDe"), NOT_FOUND)

def test_middle():
    checker = StringChecker()
    eq_(checker.first_occurrence("ABCDE", "xABCDEx"), 1)
    eq_(checker.first_occurrence("ABCDE", "xyABCDExy"), 2)
    eq_(checker.first_occurrence("ABCDE", "xyzABCDExyz"), 3)
    eq_(checker.first_occurrence("ABCDE", "xyzaABCDExyza"), 4)
    
def test_find_beginning():
    checker = StringChecker()
    eq_(checker.first_occurrence("ABCDE", "ABCDE"), 0)
    eq_(checker.first_occurrence("ABCDE", "ABCDEFGHIJ"), 0)

def test_find_end():
    checker = StringChecker()
    eq_(checker.first_occurrence("ABCDE", "ABCDE"), 0)
    eq_(checker.first_occurrence("ABCDE", "xxxxxABCDE"), 5)
    
def test_multi_occurrences():
    checker = StringChecker()
    eq_(checker.first_occurrence("ABCDE", "ABCDExxABCDEyyyABCDE"), 0)
    eq_(checker.first_occurrence("ABCDE", "xxABCDEyyyABCDE"), 2)

def test_shorter():
    checker = StringChecker()
    eq_(checker.first_occurrence("ABCDE", ""), NOT_FOUND)
    eq_(checker.first_occurrence("ABCDE", "ABCD"), NOT_FOUND)
    eq_(checker.first_occurrence("ABCDE", "BCDE"), NOT_FOUND)

def test_empty():
    checker = StringChecker()
    eq_(checker.first_occurrence("ABCDE", ""), NOT_FOUND)
    eq_(checker.first_occurrence("", "ABCDE"), 0)
    eq_(checker.first_occurrence("", ""), 0)

    eq_(checker.first_occurrence("ABCDE", None), NOT_FOUND)
    eq_(checker.first_occurrence(None, "ABCDE"), NOT_FOUND)
    eq_(checker.first_occurrence(None, None), NOT_FOUND)

def run():
    nose.run()
    
if __name__ == '__main__':
    run()

