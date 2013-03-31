"""
Test set for reverse_seq
"""
import nose
from nose.tools import eq_, ok_
from data_structures.basics.reverse_seq import do_reverse 

def test_basic():
    eq_( do_reverse([1,2,3]), [3,2,1] )
    eq_( do_reverse(["A", "B", "C", "D"]), ["D", "C", "B", "A"] )

def run():
    nose.run()
    
if __name__ == '__main__':
    run()