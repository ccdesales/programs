package com.cesarcd.tests.clients.decorators;

import com.meterware.httpunit.WebRequest;

/**
 * Decorates an HTTP Requests to append the
 * header required to trigger and test
 * License renewal
 */
public class LicenceRenewalDecorator implements IRequestDecorator {

	@Override
	public WebRequest addHeaders(WebRequest req) {
        req.setHeaderField("X-SUBSCRINFO", "ingrace");		
        return req;
	}

}
