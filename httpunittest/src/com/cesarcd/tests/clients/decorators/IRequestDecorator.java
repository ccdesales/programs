package com.cesarcd.tests.clients.decorators;

import com.meterware.httpunit.WebRequest;

/**
 * Basic contract to be implemented by decorators that
 * want to emulate a client connecting to the
 * platform using the required HTTP headers. 
 */
public interface IRequestDecorator {
	WebRequest addHeaders(WebRequest req);
}
