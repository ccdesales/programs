import shelve
from pysqlite2 import dbapi2 as sqlite

class Person:
    ap=''
    am=''
    name=''
    
    def __init__(self, ap, am, name):
        self.ap = ap
        self.am = am 
        self.name = name 
        
    def __str__(self):
        return str((self.name, self.ap, self.am))

class SaveTemplate:        
    
    def readConfig(self):
        print 'reading config'
    
    def readData(self):
        ap = raw_input('AP:')
        am = raw_input('AM:')
        name = raw_input('Name:')
        pp = Person(ap, am, name)
        return pp
        
    def saveData(self, person):
        pass
        
    def run(self):
        self.readConfig()
        pp = self.readData()
        self.saveData(pp)
        
class PickleSave(SaveTemplate):
    def saveData(self, person):
        db = shelve.open('person.dump','c')
        db['pp'] = person
        db.close()        
        print '[PickleSave] Object saved'
        
class SQLSave(SaveTemplate):
    def saveData(self, person):
        print 'Saved to SQL'
        
def testPickle():
    db = shelve.open('person.dump', 'r')
    print db['pp']


ps = PickleSave()
ps.run()
testPickle()

psql = SQLSave()
psql.run()



