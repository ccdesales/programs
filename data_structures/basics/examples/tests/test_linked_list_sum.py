'''
Created on Mar 13, 2013

@author: desales
'''

import nose
from nose.tools import ok_
from data_structures.basics.linked_list import LinkedList
from data_structures.basics.examples.linked_list_sum import LinkedListCalculator

def build_from_elements(items):
    ll = LinkedList()
    for ii in items:
        ll.insertBeginning(ii)
    return ll
"""
def int2seq(number):
    return [int(xx) for xx in str(number)]

def test_int2seq():
    op1 = int2seq(513)
    op2 = int2seq(295)
    
    print op1
    print op2
    
    ok_(op1 == [5, 1, 3])
    ok_(op2 == [2, 9, 5])
        
    ok_( int2seq(513 + 295) == int2seq(808) )
"""    

def test_sum():
    op1 = (3, 1, 5)
    op2 = (5, 9, 2)
    expected = (8, 0, 8)
    
    op1_ll = build_from_elements(op1)
    op2_ll = build_from_elements(op2)
    expected_ll = build_from_elements(expected)

    calc = LinkedListCalculator()
    result = calc.sum(op1_ll, op2_ll)
    for res, expected in zip(result.traverse() , expected_ll.traverse()):
        ok_(res == expected)

def test_traverse():
    items = ("AA", "BB", "CC")
    ll = build_from_elements(items)


    for res, expected in zip(ll.traverse() , ("CC", "BB", "AA")):
        ok_(res.cargo == expected)
    
def run():
    nose.run()
    
if __name__ == '__main__':
    run()