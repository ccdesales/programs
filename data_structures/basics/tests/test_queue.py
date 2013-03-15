import nose
from nose.tools import eq_
from data_structures.basics.queue import Queue

def test_all():
    qq = Queue()
    
    eq_(None, qq.dequeue())
    eq_(None, qq.dequeue())
    eq_(None, qq.dequeue())
    
    qq.enqueue(1)
    eq_(1, qq.dequeue())
    
    elems = [1,2,3,4,5,6,7,8,9,10]
       
    for elem in elems: 
        qq.enqueue(elem)
    
    eq_(1, qq.dequeue())
    eq_(2, qq.dequeue())
    eq_(3, qq.dequeue())
    eq_(4, qq.dequeue())
    eq_(5, qq.dequeue())
    eq_(6, qq.dequeue())
    eq_(7, qq.dequeue())
    eq_(8, qq.dequeue())
    eq_(9, qq.dequeue())
    eq_(10, qq.dequeue())
    eq_(None, qq.dequeue())
    
def run():
    nose.run()
    
if __name__ == '__main__':
    run()
