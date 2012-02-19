package com.cesarcd.tests.clients;

import java.io.IOException;

import org.xml.sax.SAXException;

import com.cesarcd.tests.clients.decorators.WAPClientDecorator;
import com.meterware.httpunit.GetMethodWebRequest;
import com.meterware.httpunit.WebConversation;
import com.meterware.httpunit.WebRequest;
import com.meterware.httpunit.WebResponse;

/**
 * Wrapper for HTTPUnit WebConversation to enable addition
 * of required HTTP headers for emulation of
 * a WAP player with access to a limited set of features. 
 */

public class WAPPlayer implements IClient {

	@Override
	public WebResponse send(String url) throws IOException, SAXException {
		WebConversation wc = new WebConversation();
        WebRequest     req = new GetMethodWebRequest(url);
		WAPClientDecorator deco = new WAPClientDecorator();
		
		req = deco.addHeaders(req);
		return wc.getResponse(req);
	}
	
	@Override
	public WebResponse send(WebRequest req) throws IOException, SAXException {
		WebConversation wc = new WebConversation();
		WAPClientDecorator deco = new WAPClientDecorator();
		
		req = deco.addHeaders(req);
		return wc.getResponse(req);
	}
	
	public WebResponse sendHead(String url) throws IOException, SAXException {
		throw new UnsupportedOperationException();
	}
}
