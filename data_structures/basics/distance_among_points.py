"""
Author: Cesar C. Desales
Created: 

"""

import operator

class DistanceCalculator:
    def are_same_sign(self, x1, x2):
        return (x1 >= 0 and x2 >= 0) or (x1 < 0 and x2 < 0)
        
    def manhatan_distance(self, point_a, point_b):
        x1, y1 = point_a
        x2, y2 = point_b
        
        xfunc = operator.sub if self.are_same_sign(x1, x2) else operator.add
        yfunc = operator.sub if self.are_same_sign(y1, y2) else operator.add
        
        xdistance = xfunc( abs(x1), abs(x2) )
        ydistance = yfunc( abs(y1), abs(y2) )
                    
        return abs(xdistance) + abs(ydistance)
    
    def is_minimal_distance(self, points):
        pass