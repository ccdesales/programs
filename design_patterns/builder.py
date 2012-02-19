import ConfigParser
from Tkinter import *

class WindowBuilder:
    config = None
    def __init__(self, filePath):
        self.config = ConfigParser.ConfigParser()
        self.config.read(filePath)
        
    def build(self):
        text = self.config.get('window', 'text')
        root = Tk()
        w = Label(root, text=text)
        w.pack()
        root.mainloop()
        
if __name__ == '__main__':                
        bb = WindowBuilder('./props.properties') 
        bb.build()
