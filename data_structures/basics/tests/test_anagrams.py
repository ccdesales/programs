"""
Test set for SetOfStacks
"""
import nose
from nose.tools import eq_, ok_
from data_structures.basics.anagrams import is_anagram 
    
def test_is_anagram():
    eq_( is_anagram("Arrigo Boito", "Tobia Gorrio"), True)
    eq_( is_anagram("Eleven plus two", "Twelve plus one"), True)
    eq_( is_anagram("I am not active", "Vacation time"), True)
    eq_( is_anagram("FOOBAR", "foobar"), True)
    eq_( is_anagram("foobar", "FOOBAR"), True)

def test_is_not_anagram():
    eq_( is_anagram("Arrigo Boito", "Tobia GorrioX"), False)
    eq_( is_anagram("Arrigo BoitoX", "Tobia Gorrio"), False)
    eq_( is_anagram("Arrigo XBoito", "Tobia Gorrio"), False)
    eq_( is_anagram("Arrigo Boito", "Tobia XGorrio"), False)
    
def run():
    nose.run()
    
if __name__ == '__main__':
    run()