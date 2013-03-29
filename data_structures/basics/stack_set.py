"""
Author: Cesar C. Desales
Created: 28 March 2013

Solution to problem from "Cracking the code Interview":
Imagine a (literal) set of plates. If the stack gets too high, it might 
topple. Therefore, in real life, we would likely start a new stack when 
the previous stack exceeds some threshold. Implement a data structure 
SetOfStacks that mimics this. SetOfStacks should be composed of several 
stacks, and should create a new stack once the previous one exceeds capacity.
"""
from Queue import LifoQueue

class SetOfStacks:
    stacks = None
    max_height = 10

    def __init__(self, max_height=10):
        self.stacks = LifoQueue()
        self.max_height = max_height 

    def num_stacks(self):
        return self.stacks.qsize()
        
    def put_nowait(self, item):
        if self.stacks.qsize() == 0:
            sub_stack = LifoQueue()
            sub_stack.put_nowait(item)
            self.stacks.put_nowait(sub_stack)
        else:
            sub_stack = self.stacks.get()
            
            if sub_stack.qsize() < self.max_height:
                sub_stack.put_nowait(item)
                self.stacks.put_nowait(sub_stack)
            else:
                newest_sub_stack = LifoQueue()
                newest_sub_stack.put_nowait(item)
                stacks.put_nowait(sub_stack)
                stacks.put_nowait(newest_sub_stack)


    def get_nowait(self):
        sub_stack = self.stacks.get_nowait()
        item = sub_stack.get_nowait()
        if not sub_stack.qsize == 0:
            self.stacks.put_nowait(sub_stack)
        return item
