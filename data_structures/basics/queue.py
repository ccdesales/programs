'''
Created on Feb 3, 2012
Module that contains the implementation of a
Queue. Notice:  The aim of this program was 
to provide the clasical implementation of this 
Data Structure, therefore neither Python lists/tuples 
nor the dequeue standard module were used.

@author: desales
'''
from doubly_linked_list import DoublyLinkedList 
class Queue:
    dlist = DoublyLinkedList()
     
    def enqueue(self, cargo):
        self.dlist.insertTail(cargo)
        
    def dequeue(self):
        return self.dlist.remove_head()