'''
Created on Jan 16, 2012

@author: desales
'''
import nose
from nose.tools import ok_, eq_ #, nottest
from ds.basics.doubly_linked_list import DoublyLinkedList

def test_insert():
    ll = DoublyLinkedList()
    ll.insertHead("AA")
    ll.insertHead("BB")
    ll.insertHead("CC")
    print ll.to_string()
    print ll.to_string(fwd=False)
    
    expected = ["CC", "BB", "AA"]
    check_elems(expected, ll)

def test_traversal():
    ll = DoublyLinkedList()
    ll.insertHead("AA")
    ll.insertHead("BB")
    ll.insertHead("CC")
    
    expected = ["CC", "BB", "AA"]
    check_elems(expected, ll)    
    
    expected = ["AA", "BB", "CC"]
    result = [elem.cargo for elem in ll.traverse_bwd()]
    ok_(result == expected, "Bad ordering in list")
    
def test_removal():
    ll = DoublyLinkedList()
    ll.insertHead("AA")
    ll.insertHead("BB")
    ll.insertHead("CC")
    ll.insertHead("DD")
    ll.insertHead("EE")
    ll.insertHead("FF")
    ll.insertHead("GG")
    
    expected = ["GG", "FF", "EE", "DD", "CC", "BB", "AA"]
    check_elems(expected, ll)    
    
    eq_("GG", ll.remove_head())
    eq_("FF", ll.remove_head())
    
    expected = ["EE", "DD", "CC", "BB", "AA"]
    check_elems(expected, ll)
    
    ok_("AA" == ll.remove_tail())
    expected = ["EE", "DD", "CC", "BB"]
    check_elems(expected, ll)

def check_elems(expected, dlist):
    result = [elem.cargo for elem in dlist.traverse_fwd()] 
    ok_(result == expected, "Bad ordering in list")

def run(): 
    nose.run() 
    
if __name__ == '__main__':
    run()