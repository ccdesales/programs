'''
Created on 09.01.2012

@author: desales
'''

class Node:
    cargo = None
    nnext = None
    pprev = None
    
    def __init__(self, cargo):
        self.cargo = cargo

    def __str__(self):
        return "<Node: %s>" % self.cargo
     
class DoublyLinkedList:
    head = None
    tail = None
    
    #---------------------------------
    # Insert operations 
    #---------------------------------
    def _insertFirst(self, cargo):
        """Insert first element of the list.
        Same procedure for inserting at the end 
        and at the beginning"""
        node = Node(cargo)
        node.pprev = None
        node.nnext = None            
        self.head = node
        self.tail = node
        
    def insertHead(self, cargo):
        """Insert at head, i.e. heads points to new node"""
        if self.is_empty():
            self._insertFirst(cargo)
        else:
            node = Node(cargo)
            self.head.nnext = node
            node.pprev = self.head
            node.nnext = None
            self.head = node        
            
    def insertTail(self, cargo):
        if self.is_empty():
            self._insertFirst(cargo)
        else:
            node = Node(cargo)
            self.tail.pprev = node
            node.nnext = self.tail
            node.pprev = None
            self.tail = node

    def to_string(self, fwd=True):
        traverse = self.traverse_fwd if fwd else self.traverse_bwd
        res = [" <-> ",]
        for node in traverse():
            res.append("[%s] <-> " % (node.cargo) )
        return "".join(res)
    
    def __str__(self):
        return self.to_string()
            
    def remove_head(self):
        if self.is_empty():
            return
        cargo = self.head.cargo
        if self.head.pprev: self.head.pprev.nnext = None
        self.head = self.head.pprev 
        return cargo
    
    def remove_tail(self):
        if self.is_empty():
            return
        cargo = self.tail.cargo
        self.tail.nnext.pprev = None                
        self.tail = self.tail.nnext
        return cargo
    
    def traverse_fwd(self):
        """Traverse from head node to tail node"""
        node = self.head
        while node:
            yield node
            node = node.pprev
            
    def traverse_bwd(self):
        """Traverse from tail node to head node"""
        node = self.tail
        while node:
            yield node
            node = node.nnext
                
    def is_empty(self):
        return self.head == None
    