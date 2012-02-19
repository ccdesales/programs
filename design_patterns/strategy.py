import time
import threading

class Context:
    pass
    
class Strategy:
    def sendSMS(self, num, text):
        pass

class SMSTask(threading.Thread):
    num = 0
    text = ''
    def run(self):
        print 'connecting...'
        print 'Sending to %s text: %s' % (self.num, self.text)        
        time.sleep(5)
        print 'Done.'
        
class AsynchStrategy(Strategy):    
    def sendSMS(self, num, text):
        task = SMSTask()
        task.num = num
        task.text = text
        task.start()
        
class SynchStrategy(Strategy):
    def sendSMS(self, num, text):
        print 'connecting...'
        print 'Sending to %s text: %s' % (num, text)
        time.sleep(5)
        print 'Done.'

syn = SynchStrategy()
for ii in range(5):
    text = '%d - %s' % (ii, 'A' * 10)
    syn.sendSMS('12345678', text)
    
    
#Asynch
#>python -u "strategy.py"
#connecting...
#Sending to 12345678 text: 0 - AAAAAAAAAA
#connecting...
#Sending to 12345678 text: 1 - AAAAAAAAAA
#connecting...
#Sending to 12345678 text: 2 - AAAAAAAAAA
#connecting...
#Sending to 12345678 text: 3 - AAAAAAAAAA
#connecting...
#Sending to 12345678 text: 4 - AAAAAAAAAA
#Done.
#Done.
#Done.
#Done.
#Done.
#>Exit code: 0


#Synch
#>python -u "strategy.py"
#connecting...
#Sending to 12345678 text: 0 - AAAAAAAAAA
#Done.
#connecting...
#Sending to 12345678 text: 1 - AAAAAAAAAA
#Done.
#connecting...
#Sending to 12345678 text: 2 - AAAAAAAAAA
#Done.
#connecting...
#Sending to 12345678 text: 3 - AAAAAAAAAA
#Done.
#connecting...
#Sending to 12345678 text: 4 - AAAAAAAAAA
#Done.
#>Exit code: 0