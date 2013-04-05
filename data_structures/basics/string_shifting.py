"""
Author: Cesar C. Desales
Created: 5 April 2013

How do you shift a String given a String 
For instance the following string abcdef and given an index 3, how would you make this in to defabc. So basically the index at a given point must be moved to the front and the rest of the string shifted to the right. 
Another example: Given an index 2 the result is cdefab
"""

def shift(ss, offset):
    ll=[]
    
    ii=offset
    while ii < len(ss):
        ll.append(ss[ii])
        ii += 1

    ii=0
    while ii < offset:
        ll.append(ss[ii])
        ii += 1

    return ''.join(ll)