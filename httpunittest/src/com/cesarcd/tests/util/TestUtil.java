package com.cesarcd.tests.util;

import java.io.IOException;

import javax.xml.parsers.ParserConfigurationException;
import javax.xml.xpath.XPathExpressionException;

import org.xml.sax.SAXException;

import com.meterware.httpunit.WebLink;

/**
 * Utility class. 
 * Works as a separation layer between Tests and 
 * the implementation of the Push XML parser
 */
public class TestUtil {

	public static void print(WebLink link) {
		System.out.println(link.getText());
		System.out.println(link.getTarget());
		System.out.println(link.getURLString());
	}

	/*
	 * Get an HTTPUnit WebLink out of a String pattern
	 */
	public static WebLink getLinkByURLPattern(WebLink[] links, String pattern) {
		for (WebLink ll : links) {			
			if (ll.getURLString().contains(pattern))
				return ll;
		}
		return null;
	}
	
	/**
	 * Method that clients can use to extract the URL
	 * element from a Push XML stream without having
	 * to interface with the XML parser and details
	 * like the XPath expression
	 */
	public static String extractContentUrl(String pushXml) throws XPathExpressionException, ParserConfigurationException, SAXException, IOException {
		String xpathExpression = "pre:push/pre:file/@url";
		XPathPushParser parser = new XPathPushParser();
		String res = parser.singleAccess(xpathExpression, pushXml, "UTF-8");
		return res;
	}
	
	/**
	 * Method that clients can use to extract the URL
	 * element from a Push XML stream without having
	 * to interface with the XML parser and details
	 * like the XPath expression
	 */
	public static String extractSubscriptionUrl(String pushXml) throws XPathExpressionException, ParserConfigurationException, SAXException, IOException {
		String xpathExpression = "pre:push/pre:subscription/@url";
		XPathPushParser parser = new XPathPushParser();
		String res = parser.singleAccess(xpathExpression, pushXml, "UTF-8");
		return res;
	}

}
