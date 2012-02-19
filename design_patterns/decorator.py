class Writer:
    def write(self, s):
        return s
        
class Upper:
    def write(self, s):
        return s.upper()
        
class Shouter:
    def write(self, s):
        return s + '!'
        
        
wr = Writer()
up = Upper()
sh = Shouter()

ss='Hola mundo'
print wr.write(up.write(sh.write(ss)))
print wr.write(sh.write(ss))