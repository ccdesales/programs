"""
Test set for SetOfStacks
"""
import nose
from nose.tools import eq_, ok_
from data_structures.basics.stack_set import SetOfStacks

def test_basic():
    qq = SetOfStacks(4)

    qq.put_nowait(1)
    qq.put_nowait("2")
    qq.put_nowait(3)

    eq_(qq.get_nowait(), 3)
    eq_(qq.get_nowait(), "2")
    eq_(qq.get_nowait(), 1)

def test_extended():
    qq = SetOfStacks(max_height=3)

    eq_(qq.num_stacks(), 0)

    qq.put_nowait("A")
    eq_(qq.num_stacks(), 1)
    qq.put_nowait("B")
    eq_(qq.num_stacks(), 1)
    qq.put_nowait("C")
    eq_(qq.num_stacks(), 1)

    qq.put_nowait("A")
    eq_(qq.num_stacks(), 2)
    qq.put_nowait("B")
    eq_(qq.num_stacks(), 2)
    qq.put_nowait("C")
    eq_(qq.num_stacks(), 2)

    qq.get_nowait()
    eq_(qq.num_stacks(), 1)
    qq.get_nowait()
    eq_(qq.num_stacks(), 1)
    qq.get_nowait()
    eq_(qq.num_stacks(), 1)
    
