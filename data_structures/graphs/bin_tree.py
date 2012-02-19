'''
Created on Feb 3, 2012

@author: desales
'''

from ds.basics.simple_pyqueue import Queue

class Tree:
    cargo   = None
    children = []
    
    def __str__(self):
        return "<%s %s>" % (self.cargo, self.children)

class BTree:
    cargo   = None
    left    = None
    right   = None
    
    def __init__(self, cargo, left, right):
        self.cargo, self.left, self.right = cargo, left, right
        
    def __str__(self):
        return "<%s %s %s>" % (self.left, self.cargo, self.right)
    
    def children(self):
        return self.left, self.right
    
def build_btree(graph):
    """Build an object based representation of a
    Binary tree from a list of nodes with references"""
    node_map = {}
    for vv, ll, rr in graph:
        tt = Tree()
        tt.cargo = vv
        tt.left  = node_map.get(ll, None)
        tt.right = node_map.get(rr, None)
        node_map[vv] = tt    
    #return the root of the tree
    return node_map[graph[-1][0]]
    
def build_tree(graph):
    """Build an object based representation of a
    Binary tree from a list of nodes with references"""
    node_map = {}
    #for vv, ll, rr in graph:
    for entry in graph:
        tt = Tree()
        tt.cargo = entry[0]
        tt.children = entry[1:]
        node_map[tt.cargo] = tt    
    #return the root of the tree
    #return node_map[graph[-1][0]]
    return node_map

    
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
    """Find element in graph, represented as a dictionary"""
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
    """Find a path to the element in the graph, represented as a dictionary"""
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
    """Find a path to the element in the graph(represented as a dictionary)
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

def breadth_first_search_tree(root):
    """Return collection of all nodes visited
    on BFS of a tree (represented as objects)"""
    path = []
    queue = Queue()
    queue.enqueue(root)
    while not queue.is_empty():
        curr = queue.dequeue()
        if not curr: break
        path.append(curr.cargo)
        for child in curr.children():
            if child: 
                queue.enqueue(child)
    return path

def BST_insert(tree,elem):
    if not tree:
        tree = BTree(elem, None, None)
    elif elem < tree.cargo:
        tree.left = BST_insert(tree.left, elem)
    else:
        tree.right = BST_insert(tree.right, elem)
    return tree

def is_line(tree):
    """Indicate if a tree is a line
    (represented as objects)"""
    print tree
    if len(tree.children) > 1:
        return False
    if len(tree.children) == 0:
        return True
    print tree.children
    return is_line(tree.children[0])
    #return False

def list2BST(elems):
    tt = None
    for elem in elems:
        tt = BST_insert(tt,elem)
    return tt