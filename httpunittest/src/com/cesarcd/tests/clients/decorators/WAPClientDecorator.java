package com.cesarcd.tests.clients.decorators;

import com.meterware.httpunit.WebRequest;

/**
 * Decorates an HTTP Requests to emulate
 * WAP client origin 
 */
public class WAPClientDecorator implements IRequestDecorator {
	@Override
	public WebRequest addHeaders(WebRequest req) {        
        req.setHeaderField("X-UP-CALLING-LINE-ID", "24234234234");
        req.setHeaderField("X-UP-SUBSCRIBER-COS", "123234234233");
        
		return req;
	}
}
