'''
Created on Mar 13, 2013

@author: desales
'''

import nose
from nose.tools import ok_
from data_structures.basics.linked_list import LinkedList

def build_from_elements(items):
    ll = LinkedList()
    for ii in items:
        ll.insertBeginning(ii)
    return ll

#def _build_linked_list():
#    items = ("AA", "BB", "CC", "DD", "EE")
#    return build_from_elements(items)


def test_traverse():
    items = ("AA", "BB", "CC")
    ll = build_from_elements(items)


    for res, expected in zip(ll.traverse() , ("AA", "BB", "CC")):
        print res, expected
        #ok_(res.cargo == expected, "Bad ordering in list")
    print "TR"
    
def run():
    nose.run()
    
if __name__ == '__main__':
    run()