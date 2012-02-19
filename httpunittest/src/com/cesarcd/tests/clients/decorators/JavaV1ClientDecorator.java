package com.cesarcd.tests.clients.decorators;

import com.meterware.httpunit.WebRequest;

/**
 * Decorates an HTTP Request to emulate
 * and old version of our Java player
 */
public class JavaV1ClientDecorator implements IRequestDecorator {

	@Override
	public WebRequest addHeaders(WebRequest req) {        
        req.setHeaderField("X-UP-CALLING-LINE-ID", "12345678900");
        req.setHeaderField("X-UP-SUBSCRIBER-COS", "234234234234");
        req.setHeaderField("X-SCREEN", "400x500");        
        req.setHeaderField("X-ACCEPT-CONTENT", "audio/apl");
        req.setHeaderField("X-PUBLIC-KEY", "SOMEKEY");
        req.setHeaderField("X-IMEI", "23232342323");
        req.setHeaderField("X-DMP-MD5", "2353453435555");
        req.setHeaderField("X-SUBSCRSTATUS", "0");
        req.setHeaderField("User-Agent", "BlackBerry9700/5.0.0 MMP-XYZ/2.12.3");
        req.setHeaderField("X-SDC-USER-AGENT", "RIM-50-Browser/BlackBerry9700/5.0.0 MMP-XYZ/2.12.3");
		return req;
		
	}

}
