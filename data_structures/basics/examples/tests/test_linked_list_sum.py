'''
Created on Mar 13, 2013

@author: desales
'''

import nose
from nose.tools import ok_
from data_structures.basics.linked_list import LinkedList
from basics.examples.linked_list_sum import LinkedListCalculator

def build_from_elements(items):
    ll = LinkedList()
    for ii in items:
        ll.insertBeginning(ii)
    return ll

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
    

def test_sum():
    op1 = (3, 1, 5)
    op2 = (5, 9, 2)
    expected_result = (8, 0, 8)
    
    left = build_from_elements(op1)
    right = build_from_elements(op2)

    calc = LinkedListCalculator()
    result_as_linked_list = calc.sum(left, right)
    for res, expected in zip(result_as_linked_list.traverse() , build_from_elements(expected_result).traverse()):
        ok_(res == expected)

def test_traverse():
    items = ("AA", "BB", "CC")
    ll = build_from_elements(items)


    for res, expected in zip(ll.traverse() , ("AA", "BB", "CC")):
        ok_(res == expected)
    print "TR"
    
def run():
    nose.run()
    
if __name__ == '__main__':
    run()