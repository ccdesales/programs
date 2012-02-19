
class Singleton:
    inst = None
    
    class Repeater:
        def repeat(self, arg):
            print arg * 2
        
    def createRepeater(self):
        if self.inst:
            return self.inst
        else:
            self.inst = self.Repeater()
            return self.inst
            
            
#rep = Repeater() #NameError: name 'Repeater' is not defined
rep = Singleton().createRepeater()
rep.repeat('abc')