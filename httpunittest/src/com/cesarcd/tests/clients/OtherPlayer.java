package com.cesarcd.tests.clients;

import java.io.IOException;

import org.xml.sax.SAXException;

import com.cesarcd.tests.clients.decorators.OtherClientDecorator;
import com.meterware.httpunit.GetMethodWebRequest;
import com.meterware.httpunit.WebConversation;
import com.meterware.httpunit.WebRequest;
import com.meterware.httpunit.WebResponse;

/**
 * Wrapper for HTTPUnit WebConversation to enable addition
 * of required HTTP headers for emulation of an unsupported client
 */
public class OtherPlayer implements IClient {

	@Override
	public WebResponse send(String url) throws IOException, SAXException {
		WebConversation wc = new WebConversation();
        WebRequest     req = new GetMethodWebRequest(url);
		OtherClientDecorator deco = new OtherClientDecorator();
		
		req = deco.addHeaders(req);
		return wc.getResponse(req);
	}
	
	public WebResponse send(WebRequest req) throws IOException, SAXException {
		WebConversation wc = new WebConversation();
		OtherClientDecorator deco = new OtherClientDecorator();
		
		req = deco.addHeaders(req);
		return wc.getResponse(req);
	}

	public WebResponse sendHead(String url) throws IOException, SAXException {
		throw new UnsupportedOperationException();
	}
}
