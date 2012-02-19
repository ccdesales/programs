package com.cesarcd.tests.clients.decorators;

import com.meterware.httpunit.WebRequest;

/**
 * Decorates an HTTP Requests to emulate
 * Android/RIM client origin (User Agent + headers)
 */
public class JavaClientDecorator implements IRequestDecorator {
	
	@Override
	public WebRequest addHeaders(WebRequest req) {        
        req.setHeaderField("X-UP-CALLING-LINE-ID", "12345678900");
        req.setHeaderField("X-UP-SUBSCRIBER-COS", "value");
        req.setHeaderField("X-SCREEN", "400x500");        
        req.setHeaderField("X-ACCEPT-CONTENT", "audio/apl");
        req.setHeaderField("X-PUBLIC-KEY", "SOME_KEY");
        req.setHeaderField("X-IMEI", "22222222222");
        req.setHeaderField("X-DMP-MD5", "ABCABCABCABCABC");
        req.setHeaderField("X-SUBSCRSTATUS", "0");
        req.setHeaderField("User-Agent", "Sony_Ericsson-LT15a/2.3.3 MMP-xyz/2.10.7");
        req.setHeaderField("X-SDC-USER-AGENT", "Android-Browser/Sony_Ericsson-LT15a/2.3.3 MMP-xyz/2.10.7");
		
        return req;
	}

}
