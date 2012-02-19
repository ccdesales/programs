from composite import Tree

class Visitable:
    def accept(visitor):
        pass
    
class VisitableTree(Tree, Visitable):
    def accept(self):        
        return self.getValue() * 2
     
class SumTreeVisitor:
    def total(self, tree):
        if tree == None: 
            return 0        
        return self.total(tree.left) + self.total(tree.right) + tree.accept()

class ConcatTreeVisitor:
    def total(self, tree):
        if tree == None: 
            return 0        
        return str(self.total(tree.left)) + str(self.total(tree.right)) + str(tree.accept())

if __name__ == '__main__':
        tree = VisitableTree(1, VisitableTree(2), VisitableTree(3)) 

        vis = SumTreeVisitor()
        print vis.total(tree)

        vis = ConcatTreeVisitor()
        print vis.total(tree)

        #>python -u "visitor.py"
        #12
        #0040062
        #>Exit code: 0

                