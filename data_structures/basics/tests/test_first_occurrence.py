"""
Test set for StringChecker
"""
import nose
from nose.tools import eq_, ok_
from data_structures.basics.first_occurrence import StringChecker

def test_not_found():
    checker = StringChecker()
    eq_(checker.first_occurrence("ABCDE", "FGHIJ"), -1)
    eq_(checker.first_occurrence("ABCDE", "aBCDE"), -1)
    eq_(checker.first_occurrence("ABCDE", "ABCDe"), -1)

def test_empty():
    checker = StringChecker()
    eq_(checker.first_occurrence("ABCDE", ""), -1)
    eq_(checker.first_occurrence("", "ABCDE"), -1)
    eq_(checker.first_occurrence("", ""), 0)

    eq_(checker.first_occurrence("ABCDE", None), -1)
    eq_(checker.first_occurrence(None, "ABCDE"), -1)
    eq_(checker.first_occurrence(None, None), -1)

def test_find_beginning():
    checker = StringChecker()
    eq_(checker.first_occurrence("ABCDE", "ABCDE"), 0)
    eq_(checker.first_occurrence("ABCDE", "ABCDEFGHIJ"), 0)

def test_find_end():
    checker = StringChecker()
    eq_(checker.first_occurrence("ABCDE", "ABCDE"), 0)
    eq_(checker.first_occurrence("ABCDE", "xxxxxABCDE"), 0)

def test_multi_occurrences():
    checker = StringChecker()
    eq_(checker.first_occurrence("ABCDE", "ABCDExxABCDEyyyABCDE"), 0)
    eq_(checker.first_occurrence("ABCDE", "xxABCDEyyyABCDE"), 2)

def test_shorter():
    checker = StringChecker()
    eq_(checker.first_occurrence("ABCDE", ""), -1)
    eq_(checker.first_occurrence("ABCDE", "ABCD"), -1)
    eq_(checker.first_occurrence("ABCDE", "BCDE"), -1)
