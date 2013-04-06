"""
Author: Cesar C. Desales

Goal: Write a program to find the first occurance of one string into another : it is okay to write a O(n2) algorithm
Created: 30/03/2013
"""
NOT_FOUND = -1

class StringChecker:
    
    def __init__(self):
        pass

    def first_occurrence(self, s1, s2):
        ii=0
        nn=0
        if s1 is None or s2 is None:
            return NOT_FOUND
        if s1 == '':
            return 0
        while ii < len(s1) and nn < len(s2):
            a, b = s1[ii], s2[nn+ii]
            if s1[ii] == s2[nn+ii]:
                return nn + self.first_occurrence(s1[ii+1:], s2[nn+ii+1:])
            else:
                nn += 1
                ii = -1
            ii += 1
        return NOT_FOUND
