"""
Proof of concept of using Java's HTTPLib from Jython
"""

from jyinterface.interfaces import JythonTesterType

from com.meterware.httpunit import (
            GetMethodWebRequest,
            WebConversation,
)
       
class JythonUnitTest(JythonTesterType):
        
    def runTest(self):
        url = 'http://example.ccom/store/mobile/landing.xhtml?VER=9115&registrationNeeded=1'
        wc = WebConversation()
        req = GetMethodWebRequest(url)
        
        req.setHeaderField("X-UP-CALLING-LINE-ID", "234234234234")
        req.setHeaderField("X-UP-SUBSCRIBER-COS", "03,plan")
        req.setHeaderField("X-SCREEN", "400x500")        
        req.setHeaderField("X-ACCEPT-CONTENT", "audio/apl")
        req.setHeaderField("X-PUBLIC-KEY", "ABC")
        req.setHeaderField("X-IMEI", "234234234")
        req.setHeaderField("X-DMP-MD5", "MIDP-346356456")
        req.setHeaderField("X-SUBSCRSTATUS", "-100")
        req.setHeaderField("User-Agent", "Sony_Ericsson-LT15a/2.3.3 MMP-Customer/2.10.7")
        req.setHeaderField("X-SDC-USER-AGENT", "Android-Browser/Sony_Ericsson-LT15a/2.3.3 MMP-Customer/2.10.7")
    
        res = wc.getResponse(req)

        print res.getText()
        print res.text

      
