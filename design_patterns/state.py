class State:
    def doAction(self):
        pass
        
class Listening(State):
    def doAction(self):
        print 'Listening for input'
        
class Opening(State):
    def doAction(self):
        print 'Openning gate'
        
class Closing(State):
    def doAction(self):
        print 'Closing gate'
        
class Context:
    state = None 
    
    def run(self):
        while True:
            inp = raw_input('>')
            print 'Input:' + inp
            
            if inp == 'cerca':
                self.state = Opening()
            elif inp == 'atraves':
                self.state = Listening()
            elif inp == 'paso':
                self.state = Closing()
            elif inp == 'stop' or inp == 'quit':
                return
            else:
                self.state = Listening()
                
            self.state.doAction()
            
ctx = Context()
ctx.run()