import sys
from socket import *

class PowerProxy:    
    serverHost = 'localhost'            # servername is localhost
    serverPort = 2000                   # use arbitrary port > 1024

    def sendRequest(self, value):
        s = socket(AF_INET, SOCK_STREAM)    # create a TCP socket

        s.connect((self.serverHost, self.serverPort)) # connect to server on the port                
        s.send(str(value))               # send the data
        data = s.recv(1024)                 # receive up to 1K bytes
        return data


class Client:
    proxy = PowerProxy()
    def sendReq(self, value):
        return self.proxy.sendRequest(value)
        
cli = Client()
print cli.sendReq(25)

#>python -u "proxy.py"
#echo -> 625
#>Exit code: 0