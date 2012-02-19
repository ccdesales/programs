class Command:
    def execute(self):
        pass
    
class UpCommand:
    def execute(self):
        print 'Cutting up'

class DownCommand:
    def execute(self):
        print 'Cutting down'
        
class LeftCommand:
    def execute(self):
        print 'Cutting left'

class RightCommand:
    def execute(self):
        print 'Cutting right'

class CommandProcessor:
    pass
    
class CuttingMachine(CommandProcessor):
    def run(self, cmdList):
        for cmd in cmdList:
            cmd.execute()            
            
if __name__ == '__main__':
        cmds = [RightCommand(), RightCommand(), DownCommand(), LeftCommand(), LeftCommand(), UpCommand()]
        machine = CuttingMachine()
        machine.run(cmds)