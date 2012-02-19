class Event:
    pass

class Observer:
    name = ''
    
    def __init__(self, name):
        self.name = name
        
    def update(self, event):
        print '[', self.name, ']Subject updated:', event.value, event.text
    
class Observable:
    pass
    
class Subject(Observable):
    #count, and notify observers each time a "notyfy" message is sent
    
    def __init__(self):
        self.observers=[]

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self, event):
        for x in self.observers:
            x.update(event)
            
    def run(self):
        for ii in range(71):
            if ii % 7 == 0:
                evt = Event()
                evt.value = ii
                evt.text = 'Can divide by 7'
                self.notify(evt)

ob1 = Observer('OBS1')
ob2 = Observer('OBS2')

subj = Subject()
subj.attach(ob1)
subj.attach(ob2)
subj.run()