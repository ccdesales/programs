'''
Created on Feb 3, 2012

@author: desales
'''
 
class Queue:
    dlist = []
    
    def __init__(self):
        self.dlist = []
        
    def enqueue(self, cargo):
        self.dlist.append(cargo)
        
    def enqueue_multi(self, cargo_list):
        for elem in cargo_list:
            self.enqueue(elem)
            
    def dequeue(self):
        if self.dlist:
            return self.dlist.pop(0)
        else:
            return None
    
    def is_empty(self):
        return self.dlist == []