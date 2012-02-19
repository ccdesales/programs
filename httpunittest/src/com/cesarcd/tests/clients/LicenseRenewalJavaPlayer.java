package com.cesarcd.tests.clients;

import java.io.IOException;

import org.xml.sax.SAXException;

import com.cesarcd.tests.clients.decorators.JavaClientDecorator;
import com.cesarcd.tests.clients.decorators.LicenceRenewalDecorator;
import com.meterware.httpunit.GetMethodWebRequest;
import com.meterware.httpunit.WebConversation;
import com.meterware.httpunit.WebRequest;
import com.meterware.httpunit.WebResponse;

/**
 * Wrapper for HTTPUnit WebConversation to enable addition
 * of required HTTP headers for emulation of
 * client on the very specific case of being 
 * in the need to trigger license acquisition
 */
public class LicenseRenewalJavaPlayer implements IClient {

	@Override
	public WebResponse send(String url) throws IOException, SAXException {
		WebConversation wc = new WebConversation();
        WebRequest     req = new GetMethodWebRequest(url);
		JavaClientDecorator deco = new JavaClientDecorator();
		LicenceRenewalDecorator deco2 = new LicenceRenewalDecorator();
		
		req = deco.addHeaders(
			deco2.addHeaders(req)
		);
		return wc.getResponse(req);
	}
	
	@Override
	public WebResponse send(WebRequest req) throws IOException, SAXException {
		WebConversation wc = new WebConversation();
		JavaClientDecorator deco = new JavaClientDecorator();
		LicenceRenewalDecorator deco2 = new LicenceRenewalDecorator();
		
		req = deco.addHeaders(
				deco2.addHeaders(req)
			);
		return wc.getResponse(req);
	}
	
	@Override
	public WebResponse sendHead(String url) throws IOException, SAXException {
		throw new UnsupportedOperationException();
	}

}
