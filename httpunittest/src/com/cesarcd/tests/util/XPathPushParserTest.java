package com.cesarcd.tests.util;



import java.io.IOException;
import java.util.ArrayList;

import javax.xml.parsers.ParserConfigurationException;
import javax.xml.xpath.XPathExpressionException;

import org.junit.*;
import org.xml.sax.SAXException;

import static org.junit.Assert.*;

/**
 * Simple class with embedded XML to test the XML Parsing component
 */
public class XPathPushParserTest {
	
	@Before 
	public void setUp() {
	}
	
	/*
	 * Test parsing of Push XML content with namespaces  
	 */
	@Test
	public void test_playerLanding() throws XPathExpressionException, ParserConfigurationException, SAXException, IOException {
		String xml = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n" +
				"<push xmlns=\"http://www.abc.com/sync-1\">\n" + 
				"<file url=\"http://example.com/Prelisten/encoding/apl/id/1-9-1217595-1-11.apl\"\n"+
				"title=\"Someone Like You\"\n" +
				"artist=\"ADELE\"\n" +
				"album=\"21\"\n" +
				"track=\"11/11\"\n" +
				"duration=\"30\"\n" +
				"action=\"stream\"\n" +
				">FILE</file>" +
				"PUSH" +
				"</push>";
		
		xml = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n" +
		//"<push>\n" + 
		"<push xmlns=\"http://www.abc.com/sync-1\">\n" + 
		"<file url=\"http://example.ccom/Prelisten/encoding/apl/id/1-9-1217595-1-11.apl\"\n"+
		"title=\"Someone Like You\"\n" +
		"artist=\"ADELE\"\n" +
		"album=\"21\"\n" +
		"track=\"11/11\"\n" +
		"duration=\"30\"\n" +
		"action=\"stream\"\n" +
		"/>" +
		"</push>";
		
		String xpathExpression = "pre:push/pre:file/@url";
		XPathPushParser parser = new XPathPushParser();
		String res = parser.singleAccess(xpathExpression, xml, "UTF-8");
		assertEquals("http://example.com/Prelisten/encoding/apl/id/1-9-1217595-1-11.apl", res);
	}
	
	/*
	 * Test an XML stream without namespaces
	 * Simpler user case.
	 */
	@Test
	public void test_XPathPushParser2() throws XPathExpressionException, ParserConfigurationException, SAXException, IOException {
		String xml = "<inventory>" + 
		  "    <book year=\"2000\">" +
		  "        <title>Snow Crash</title>" +
		  "        <author>Neal Stephenson</author>" +
		  "        <publisher>Spectra</publisher>" +
		  "        <isbn>0553380958</isbn>" +
		  "        <price>14.95</price>" +
		  "    </book>" +
		  "    <book year=\"2005\">" +
		  "        <title>Burning Tower</title>" +
		  "        <author>Larry Niven</author>" +
		  "        <author>Jerry Pournelle</author>" +
		  "        <publisher>Pocket</publisher>" +
		  "        <isbn>0743416910</isbn>" +
		  "        <price>5.99</price>" +
		  "    </book>" +
		  "    <book year=\"1995\">" +
		  "        <title>Zodiac</title>" +
		  "        <author>Neal Stephenson</author>" +
		  "        <publisher>Spectra</publisher>" +
		  "        <isbn>0553573862</isbn>" +
		  "        <price>7.50</price>" +
		  "    </book>" +
		  "    <!-- more books... -->" +
		  "</inventory>";		
		
		String xpathExpression = "//book[author='Neal Stephenson']/title/text()";
		XPathPushParser parser = new XPathPushParser();
		ArrayList<String> res = parser.multiAccess(xpathExpression, xml, "UTF-8");
		assertEquals(res.get(0), "Snow Crash"); 
		assertEquals(res.get(1), "Zodiac");		
	}	
}