import random

class Generator:
    handler = None
    def run(self):
        for ii in range(5):
            evt = random.choice(['debug', 'info', 'warning', 'error'])
            self.handler.handle(evt + str(ii))

class Handler:
    def handle(self, evt):
        pass
        
class DebugHandler(Handler):
    next = None
    def __init__(self, next=None):
        self.next = next        
    def handle(self, evt):        
        print 'DEBUG, write to log', evt 
        self.next.handle(evt)        

class InfoHandler(Handler):
    next = None
    def __init__(self, next=None):
        self.next = next
    def handle(self, evt):
        if 'info' in evt:
            print 'INFO, play beep', evt
            return
        else:
            self.next.handle(evt)

class WarningHandler(Handler):
    next = None
    def __init__(self, next=None):
        self.next = next
    def handle(self, evt):
        if 'warning' in evt:
            print 'WARNING, send email', evt
            return
        else:
            self.next.handle(evt)

class ErrorHandler(Handler):
    next = None
    def __init__(self, next=None):
        self.next = next
    def handle(self, evt):
        if 'error' in evt:
            print 'ERROR, send SMS', evt
       
                
ee = ErrorHandler()
ww = WarningHandler(ee)
ii = InfoHandler(ww)
dd = DebugHandler(ii)

gg = Generator()
gg.handler = dd
gg.run()

#>python -u "chor.py"
#DEBUG, write to log debug0
#DEBUG, write to log error1
#ERROR, send SMS error1
#DEBUG, write to log warning2
#WARNING, send email warning2
#DEBUG, write to log info3
#INFO, play beep info3
#DEBUG, write to log warning4
#WARNING, send email warning4
#>Exit code: 0

