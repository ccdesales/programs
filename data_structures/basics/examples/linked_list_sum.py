'''
Created on Mar 13, 2013
Program that implements aritmetic operation on
linked list representing integer numbers

@author: desales
'''
from data_structures.basics.linked_list import LinkedList

class LinkedListCalculator:
    def sum(self, lla, llb):
        carry = 0
        ll = LinkedList()
        
        for op1, op2 in zip(lla.traverse() , llb.traverse()):
            res = carry + op1.cargo + op2.cargo
            curr_digit = res%10
            carry = res / 10
            ll.insertBeginning(curr_digit)
        return ll
