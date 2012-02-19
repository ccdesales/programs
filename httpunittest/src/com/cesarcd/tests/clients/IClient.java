package com.cesarcd.tests.clients;

import java.io.IOException;

import org.xml.sax.SAXException;

import com.meterware.httpunit.WebRequest;
import com.meterware.httpunit.WebResponse;

public interface IClient {
	WebResponse send(String url) throws IOException, SAXException;	
	WebResponse send(WebRequest req) throws IOException, SAXException;
	WebResponse sendHead(String url) throws IOException, SAXException;
}
