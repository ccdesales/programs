'''
Created on Feb 3, 2012
Module that contains the Tree data type
and related methods to traverse and
process nodes.

@author: desales
'''

from ds.basics.simple_pyqueue import Queue

class Tree:
    cargo   = None
    left    = None
    right   = None
        
    def __str__(self):
        return "<%s %s %s>" % (self.left, self.cargo, self.right)
    
def build(graph):
    node_map = {}
    for vv, ll, rr in graph:
        tt = Tree()
        tt.cargo = vv
        tt.left  = node_map.get(ll, None)
        tt.right = node_map.get(rr, None)
        node_map[vv] = tt    
    #return the root of the tree
    return node_map[graph[-1][0]]
    
    
def in_order(tree, callback):
    if tree:
        in_order(tree.left, callback)
        callback( tree.cargo )
        in_order(tree.right, callback)

def pre_order(tree, callback):
    if tree:
        callback( tree.cargo )
        pre_order(tree.left, callback)
        pre_order(tree.right, callback)
        
def post_order(tree, callback):
    if tree:
        post_order(tree.left, callback)
        post_order(tree.right, callback)
        callback( tree.cargo )
        
def find(elem, tree):
    """Binary search on binary search tree"""
    if not elem:
        return 
    elif elem == tree.cargo:
        return elem
    elif elem < tree.cargo:
        return find(elem, tree.left)
    else: #if elem > tree.cargo:
        return find(elem, tree.right)

def breadth_first_search(term, root, graph):
    """Find element in graph"""
    queue = Queue()
    queue.enqueue(root)
    curr = queue.dequeue()
    while curr:
        if curr == term:
            return curr
        else:
            queue.enqueue_multi(graph[curr])
        curr = queue.dequeue()
    return None #Not found

def breadth_first_search_path(term, root, graph):
    """Find a path to the element in the graph"""
    path = []
    queue = Queue()
    queue.enqueue(root)
    while not queue.is_empty():
        curr = queue.dequeue()
        if not curr in path:
            path.append(curr)
        if curr == term:
            return path
        else:
            queue.enqueue_multi(graph[curr])
    return None #Not found

def depth_first_search(term, root, graph, path=[]):
    """Find element in graph"""
    path = path + [root]
    if term == root:
        return path
    children = graph[root]
    for child in children:
        res = depth_first_search(term, child, graph, path)
        if res:
            return res
    return None

def max_depth(root, graph):
    """get max lengh in a binary tree"""
    if not root:
        return 0
    left, right = graph[root]
    return 1 + max(
        max_depth(left, graph),
        max_depth(right, graph)
    )
    
def min_depth(root, graph):
    """get max lengh in a binary tree"""
    if not root:
        return 0
    left, right = graph[root]
    return 1 + min(
        min_depth(left, graph),
        min_depth(right, graph)
    )

def is_balanced(root, graph):
    """determine if a binary tree is balanced"""
    return max_depth(root, graph) - min_depth(root, graph) <=1;

def range_filter(value, lower, upper):
    return value >= lower and value <= upper

def breadth_first_search_filter(root, ffilter, filter_args, graph):
    """Find a path to the element in the graph
    TODO: Return paths instead of nodes"""    
    res = []
    queue = Queue()
    queue.enqueue(root)
    while not queue.is_empty():
        curr = queue.dequeue()       
        if ffilter(curr, **filter_args):
            res.append(curr)
        queue.enqueue_multi(graph[curr])
    return res