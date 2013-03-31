"""
Author: Cesar C. Desales
Created: 

"""

def do_reverse(seq):
    
    if len(seq):
        return [seq[-1]] + do_reverse(seq[:-1])
    else:
        return type(seq)()