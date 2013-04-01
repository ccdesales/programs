"""
Author: Cesar C. Desales
Created: 

"""

def is_anagram(s1, s2):
    s1 = s1.lower().replace(' ', '')
    s2 = s2.lower().replace(' ', '')
    
    if len(s1) != len(s2):
        return False
    
    counter = dict()
    for cc in s1:
        count = counter.get(cc, 0)
        counter[cc] = count+1
    
    for cc in s2:
        count = counter.pop(cc, 0)
        if not count:
            return False
        
        count=count-1
        if count > 0:
            counter[cc] = count

    return not counter