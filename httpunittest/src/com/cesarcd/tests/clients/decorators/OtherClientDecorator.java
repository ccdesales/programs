package com.cesarcd.tests.clients.decorators;

import com.meterware.httpunit.WebRequest;

/**
 * Decorates an HTTP Requests to emulate
 * unsupported client origin (no additional
 * headers provided, access denied) 
 */
public class OtherClientDecorator implements IRequestDecorator {

	@Override
	public WebRequest addHeaders(WebRequest req) {
		return req;
	}

}
