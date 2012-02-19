class Tree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    def getValue(self):
        return self.value
    def __str__(self):
        return str(self.value)

if __name__ == '__main__':
        left = Tree(2)
        right = Tree(3)        
        tree = Tree(1, left, right)
        tree = Tree(1, Tree(2), Tree(3)) 