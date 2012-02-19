class TransactionManager:
    nodes = []
    precommited = []
    rejected = []
        
    def register(self, node):
        self.nodes.append(node)
    
    def preCommit(self):
        for node in self.nodes:
            if node.preCommit():
                self.precommited.append(node)
            else:
                self.rejected.append(node)
                
    def commit(self):
        if len(self.rejected) == 0:
            for node in self.precommited:
                node.commit()
        else:
            for node in self.rejected:
                node.rollback()
                
    def runTransaction(self):
        self.preCommit()
        self.commit()

class DBNode:
    name = ''
    def preCommit(self):
        print self.name, 'precommiting' 
        return True    
    def commit(self):
        print self.name, 'commiting' 
        return True
    def rollback(self):
        print self.name, 'rolling back' 
        return True
    
n1 = DBNode()
n2 = DBNode()
n3 = DBNode()

tm = TransactionManager()
tm.register(n1)
tm.register(n2)
tm.register(n3)

tm.runTransaction()