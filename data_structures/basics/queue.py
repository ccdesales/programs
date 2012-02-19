'''
Created on Feb 3, 2012

@author: desales
'''
from doubly_linked_list import DoublyLinkedList 
class Queue:
    dlist = DoublyLinkedList()
     
    def enqueue(self, cargo):
        self.dlist.insertTail(cargo)
        
    def dequeue(self):
        return self.dlist.remove_head()