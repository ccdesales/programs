from jyinterface.interfaces import EmployeeType

class Employee(EmployeeType):
   def __init__(self, first, last, id):
      self.first = first
      self.last  =  last
      self.id = id

   def getEmployeeFirst(self):
      return self.first

   def getEmployeeLast(self):
      return self.last

   def getEmployeeId(self):
      return self.id