package com.cesarcd.tests.clients;

import java.io.IOException;

import org.xml.sax.SAXException;

import com.cesarcd.tests.clients.decorators.JavaClientDecorator;
import com.meterware.httpunit.GetMethodWebRequest;
import com.meterware.httpunit.HeadMethodWebRequest;
import com.meterware.httpunit.WebConversation;
import com.meterware.httpunit.WebRequest;
import com.meterware.httpunit.WebResponse;

/**
 * Wrapper for HTTPUnit WebConversation to enable addition
 * of required HTTP headers for emulation of
 * Android/RIM clients
 */
public class JavaPlayer implements IClient {

	@Override
	public WebResponse send(String url) throws IOException, SAXException {
		WebConversation wc = new WebConversation();
        WebRequest     req = new GetMethodWebRequest(url);
		JavaClientDecorator deco = new JavaClientDecorator();
		
		req = deco.addHeaders(req);
		return wc.getResponse(req);
	}
	
	@Override
	public WebResponse send(WebRequest req) throws IOException, SAXException {
		WebConversation wc = new WebConversation();
		JavaClientDecorator deco = new JavaClientDecorator();
		
		req = deco.addHeaders(req);
		return wc.getResponse(req);
	}
	
	@Override
	public WebResponse sendHead(String url) throws IOException, SAXException {
		WebConversation wc = new WebConversation();
        WebRequest     req = new HeadMethodWebRequest(url);
		
		return wc.getResponse(req);
	} 

}
