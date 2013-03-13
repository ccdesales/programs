import nose
from nose.tools import ok_
from data_structures.basics.linked_list import LinkedList

#-------------------------------
# Sample runs of Linked List methods
#-------------------------------

def build_from_elements(items):
    ll = LinkedList()
    for ii in items:
        ll.insertBeginning(ii)
    return ll

def _build_linked_list():
    items = ("AA", "BB", "CC", "DD", "EE")
    return build_from_elements(items)

def test_direct_remove():
    ll = _build_linked_list()
    ll.direct_remove("EE")
    ll.direct_remove("AA") #Tail cannot be directly removed
    ll.direct_remove("CC")
    
    expected = ["DD", "BB", "AA"]    
    result = [elem.cargo for elem in ll.traverse()] 
    ok_(result == expected, "Bad ordering in list")    
    
    expected = ["DD", "BB"]
    ok_(result != expected, "Bad ordering in list")
        
def test_remove():
    ll = _build_linked_list()
    for item in ("BB", "DD", "EE", "AA", "CC"):
        ll.remove(item)
    
    ok_(ll.is_empty(), "Not empty")
    ll.remove("CC")
    ok_(ll.is_empty(), "Not empty")
        
def test_remove_after():
    ll = _build_linked_list()
    ll.remove_after("CC")
    expected = ("EE", "DD", "CC", "AA")
    
    for res, expected in zip(ll.traverse(), expected):
        ok_(res.cargo == expected, "Bad ordering in list")

def test_find():
    ll = _build_linked_list()
    ok_("CC", ll.find("CC"))

def test_is_Empty():
    ll = LinkedList()
    ok_(ll.is_empty(), "Not empty")
    ll.insertBeginning("XX")
    ok_(not ll.is_empty(), "Empty!")
        
def test_insertBeginning():
    items    = ("AA", "BB", "CC")
    expected = reversed(items)
    
    ll = LinkedList()
    for ii in items:
        ll.insertBeginning(ii)
    
    for res, expected in zip(ll.traverse(), expected):
        ok_(res.cargo == expected, "Bad ordering in list")

    
def test_insertAfter():
    ll = LinkedList()
    ll.insertBeginning("CC")
    ll.insertBeginning("AA") 
    ll.insertAfter("AA", "BB")

    for res, expected in zip(ll.traverse() , ("AA", "BB", "CC")):
        ok_(res.cargo == expected, "Bad ordering in list")

def run():
    nose.run()
    
if __name__ == '__main__':
    run()
