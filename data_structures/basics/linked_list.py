'''
Created on 09.01.2012
Module that contains the implementation of a
Linked List. Notice: Regular python lists 
or tuples were not used for this program as the 
intend was to provide the clasical implementation
that does not rely on the availability of such a
powerful built-in data structure

@author: desales
'''

class Node:
    cargo = None
    nnext = None
    
    def __init__(self, cargo):
        self.cargo = cargo

    def __str__(self):
        return "<Node: %s>" % self.cargo
     
class LinkedList:
    firstNode = None
    
    #---------------------------------
    # Insert operations 
    #---------------------------------
    def insertBeginning(self, cargo):
        self._insertBeginning(Node(cargo))
        
    def _insertBeginning(self, newNode):
        newNode.nnext = self.firstNode
        self.firstNode = newNode
    
    def insertAfter(self, cargo, newCargo):
        self._insertAfter(self._find(cargo), Node(newCargo))
        
    def _insertAfter(self, node, newNode):
        newNode.nnext = node.nnext
        node.nnext = newNode
    
    def find(self, cargo):
        """Redundant, implemented to demonstrate _find"""
        return self._find(cargo).cargo 
    
    def _find(self, cargo):
        for node in self.traverse():
            if node.cargo == cargo:
                return node
        return
    
    def __str__(self):
        res = []
        for node in self.traverse():
            res.append("[%s] -> " % (node.cargo) )
        return "".join(res)
    
    def remove_node_after(self, node):
        self.remove_after(self, node.cargo)
        
    def remove_after(self, cargo):
        node = self.firstNode
        while node:
            if node.cargo == cargo:
                node.nnext = node.nnext.nnext
            node = node.nnext
    
    def direct_remove(self, cargo):
        node = self._find(cargo)
        if not node:
            return
        
        if node.nnext:
            node.cargo = node.nnext.cargo
            node.nnext = node.nnext.nnext
        else: #tail
            node = None
            #NOTE: This problem can not be solved if the node to be deleted 
            #is the last node in the linked list. 
        
    def remove(self, cargo):
        if not self.firstNode:
            return 
        
        if cargo == self.firstNode.cargo:
            self.firstNode = self.firstNode.nnext
            return
        
        node = self.firstNode
        while node:
            if node.nnext:
                if cargo == node.nnext.cargo:
                    node.nnext = node.nnext.nnext 
                    return
            node = node.nnext
            
    def traverse(self):
        node = self.firstNode
        while node:
            yield node
            node = node.nnext
                
    def is_empty(self):
        return self.firstNode == None
    