import math

class MathAdapter:    
    def sqrt(self, alist):
        res = []
        for ii in alist:
            res.append(math.sqrt(ii))
        return res
        
ma = MathAdapter()
print ma.sqrt([25, 16, 4])
            
    