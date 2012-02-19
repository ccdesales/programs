"""
Module to test via Nose the usage
of the Tree data type
and related methods to traverse and
process nodes.
"""

import nose
from nose.tools import ok_, eq_, nottest
from ds.graphs.bin_tree import (
    find,
    build,
    in_order,
    min_depth,
    max_depth,
    pre_order,
    post_order,
    is_balanced,    
    depth_first_search,
    breadth_first_search, 
    breadth_first_search_path,    
)

elems = []
def do_store(oo):
    global elems
    elems.append(oo)
    
def test_inorder():
    global elems
    elems = []
    graph = (
        ["A", None, None],
        ["C", None, None],
        ["E", None, None],
        ["G", None, None],
        ["B", 'A', 'C'],
        ["F", 'E', 'G'],
        ["D", 'B', 'F'],
    )    
    
    tree = build(graph)
    in_order(tree, callback=do_store)
    
    eq_(elems, ['A', 'B', 'C', 'D', 'E', 'F', 'G'])

def test_preorder():
    global elems
    elems = []
    graph = (
        ["A", None, None],
        ["C", None, None],
        ["E", None, None],
        ["G", None, None],
        ["B", 'A', 'C'],
        ["F", 'E', 'G'],
        ["D", 'B', 'F'],
    )    
    
    tree = build(graph)
    pre_order(tree, callback=do_store)
    
    eq_(elems, ['D', 'B', 'A', 'C', 'F', 'E', 'G'])
    
def test_post_order():
    global elems
    elems = []
    graph = (
        ["A", None, None],
        ["C", None, None],
        ["E", None, None],
        ["G", None, None],
        ["B", 'A', 'C'],
        ["F", 'E', 'G'],
        ["D", 'B', 'F'],
    )    
    
    tree = build(graph)
    post_order(tree, callback=do_store)
    
    eq_(elems, ['A', 'C', 'B', 'E', 'G', 'F', 'D'])

def test_non_balanced():
    global elems
        
    graph = (
        [9, None, None],
        [8, None, None],
        [7, 8, None],
        [6, 7, 9],
        [5, None, None],
        [4, 5, 6],
        [3, None, None],
        [2, 3, None],
        [1, 2, 4],
    )    
    
    tree = build(graph)
    
    elems = []
    pre_order(tree, callback=do_store)
    eq_(elems, [1,2,3,4,5,6,7,8,9])
    
    elems = []
    in_order(tree, callback=do_store)
    eq_(elems, [3,2,1,5,4,8,7,6,9])
    
    elems = []
    post_order(tree, callback=do_store)
    eq_(elems, [3,2,5,8,7,9,6,4,1])
    
def test_find():
    global elems
        
    graph = (
        [3, None, None],
        [14, 3, None],
        [10, None, 14],
        [4, None, None],
        [7, None, None],
        [6,4,7],
        [1,None, None],
        [3,1,6],
        [8,3,10],
    )    
 
    tree = build(graph)
    eq_(None, find(None, tree))
    eq_(8, find(8, tree))
    eq_(7, find(7, tree))

def test_breadth_first_search():
    graph = dict(
        A = ("B", "C"),
        B = ("F", "D"),
        C = ("F", "E"),
        D = ("E"),
        E = (),
        F = (),
    )
    root = "A"
    
    eq_("A", breadth_first_search(term="A", root=root, graph=graph)) #find root
    eq_("E", breadth_first_search(term="E", root=root, graph=graph))
    eq_(None, breadth_first_search(term="N", root=root, graph=graph)) #find unexistent element
     
def test_breadth_first_search_path():
    graph = dict(
        A = ("B", "C"),
        B = ("F", "D"),
        C = ("F", "E"),
        D = ("E"),
        E = (),
        F = (),
    )
    root = "A"
    
    eq_(["A"], breadth_first_search_path(term="A", root=root, graph=graph)) #find root
    eq_(["A", "B", "C"], breadth_first_search_path(term="C", root=root, graph=graph))
    eq_(["A", "B", "C", "F", "D"], breadth_first_search_path(term="D", root=root, graph=graph))
    eq_(["A", "B", "C", "F", "D", "E"], breadth_first_search_path(term="E", root=root, graph=graph))
    eq_(None, breadth_first_search_path(term="N", root=root, graph=graph)) #find unexistent element

def test_breadth_first_search_path2():
    graph = dict(
        A = ("B", "C"),
        B = ("M", "F", "D"),
        D = ("E", "N", "F", "O"),
        C = ("F", "E"),
        M = ("N", "F"),
        F = ("N"),
        N = (),
        O = (),
        E = (),
    )
    root = "A"
    
    eq_(["A"], breadth_first_search_path(term="A", root=root, graph=graph)) #find root
    eq_(["A", "B", "C"], breadth_first_search_path(term="C", root=root, graph=graph))
    eq_(["A", "B", "C", "M", "F", "D"], breadth_first_search_path(term="D", root=root, graph=graph))
    eq_(["A", "B", "C", "M", "F", "D", "E"], breadth_first_search_path(term="E", root=root, graph=graph))
    eq_(["A", "B", "C", "M", "F", "D", "E", "N", "O"], breadth_first_search_path(term="O", root=root, graph=graph))
    eq_(None, breadth_first_search_path(term="Missing", root=root, graph=graph)) #find unexistent element

def test_depth_first_search():
    graph = dict(
        A = ("B", "C"),
        B = ("F", "D"),
        C = ("F", "E"),
        D = ("E"),
        E = (),
        F = (),
    )
    root = "A"
    eq_(["A"], depth_first_search(term="A", root=root, graph=graph)) #find root
    eq_(["A", "B"], depth_first_search(term="B", root=root, graph=graph)) 
    eq_(['A', 'B', 'D', 'E'], depth_first_search(term="E", root=root, graph=graph))
    eq_(None, depth_first_search(term="N", root=root, graph=graph)) #find unexistent element

def test_depth_first_search2():
    graph = dict(
        A = ("B", "C"),
        B = ("M", "F", "D"),
        D = ("E", "N", "F", "O"),
        C = ("F", "E"),
        M = ("N", "F"),
        F = ("N"),
        N = (),
        O = (),
        E = (),
    )
    
    root = "A"
    eq_(["A"], depth_first_search(term="A", root=root, graph=graph)) #find root
    eq_(["A", "B"], depth_first_search(term="B", root=root, graph=graph)) 
    eq_(['A', 'B', 'D', 'E'], depth_first_search(term="E", root=root, graph=graph))
    eq_(['A', 'B', 'M', 'N'], depth_first_search(term="N", root=root, graph=graph))
    eq_(None, depth_first_search(term="Missing", root=root, graph=graph)) #find unexistent element

def test_depth_ops():
    graph = dict(
        A = ("B", "C"),
        B = ("D", "E"),
        C = ("F", "G"),
        D = (None, "H"),
        H = (None, None),
        E = (None, None),
        F = ("I", None),
        G = (None, None),
        I = (None, None),
    )
    root = "A"
    eq_(3, min_depth(root, graph))
    eq_(4, max_depth(root, graph))
    ok_(is_balanced(root, graph))
    
    graph["H"] = ("J", None)
    graph["J"] = (None, None)
    
    min_depth(root, graph)
    max_depth(root, graph)
    
    ok_(not is_balanced(root, graph))
    
def test_find_path():
    graph = dict(
        A = ("B", "C"),
        B = ("M", "F", "D"),
        D = ("E", "N", "F", "O"),
        C = ("F", "E"),
        M = ("N", "F"),
        F = ("N"),
        N = (),
        O = (),
        E = (),
    )
    
    #Tests with the tree's root as the departing point are included in a different section
    
    eq_(["B"], breadth_first_search_path(root="B", term="B", graph=graph))
    eq_(["B", "M", "F"], breadth_first_search_path(root="B", term="F", graph=graph)) 
    eq_(["B", "M", "F", "D", "N"], breadth_first_search_path(root="B", term="N", graph=graph))
    eq_(["C", "F", "E", "N"], breadth_first_search_path(root="C", term="N", graph=graph))
    
    eq_(None, breadth_first_search_path(root="C", term="M", graph=graph))
    eq_(None, breadth_first_search_path(root="E", term="B", graph=graph))

def test_select_range_path():
    graph = {
        1 : (2, 5),
        2 : (3, 4),
        3 : (),
        4 : (),
        5 : (6, 7),
        6 : (),
        7 : (),
    }
    root = 1
    
    from ds.graphs.bin_tree import breadth_first_search_filter, range_filter
    
    kwargs = dict(
         lower = 3,
         upper = 6
    )
    
    eq_([5,3,4,6], breadth_first_search_filter(root, range_filter, kwargs, graph))
    
def test_select_range_path2():
    graph = {
        1 : (8, 2, 11, 5),
        2 : (3, 4),
        3 : (),
        4 : (),
        5 : (6, 7),
        6 : (),
        7 : (),
        8 : (9, 10),
        9 : (),
        10 : (),
        11 : (12, 13),
        12 : (),
        13 : (14, 15),
        14 : (),
        15 : (16, 17),
        16 : (),
        17 : (),
    }
    root = 1
    
    from ds.graphs.bin_tree import breadth_first_search_filter, range_filter
    
    kwargs = dict(
         lower = 6,
         upper = 13
    )
    
    eq_([8,11,9,10,12,13,6,7], breadth_first_search_filter(root, range_filter, kwargs, graph))

        
def run():    
    nose.run()
    
if __name__ == '__main__':
    run()
