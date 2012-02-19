package com.cesarcd.tests.util;

import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.ArrayList;

import org.w3c.dom.*;
import org.xml.sax.SAXException;

import javax.xml.parsers.*;
import javax.xml.xpath.*;

/**
 * Class to parse Push XML content to extract 
 * data specified through an specific XPath expression
 */
public class XPathPushParser {	
	/* 
	 * Build an XML document out of an String
	 * representing the content and an specific encoding
	 */
	private Document buildDocument(String xml, String encoding) throws ParserConfigurationException, SAXException, IOException {
		InputStream is = new ByteArrayInputStream(xml.getBytes(encoding));
		
	    DocumentBuilderFactory domFactory = DocumentBuilderFactory.newInstance();
	    domFactory.setNamespaceAware(true); // never forget this!
	    DocumentBuilder builder = domFactory.newDocumentBuilder();
	    Document doc = builder.parse(is);
	    return doc;
	}
	
	/*
	 * Take an XPath expression and convert it to an object
	 * suitable to be used by the XML parser
	 */
	private XPathExpression buildXPathExpression(String xpathExpression) throws XPathExpressionException {
		XPathFactory factory = XPathFactory.newInstance();
	    XPath xpath = factory.newXPath();
	    xpath.setNamespaceContext(new CustomNamespaceContext());
	    XPathExpression expr = xpath.compile(xpathExpression);
	    return expr;
	}

	/* 
	 * Evaluate the Xpath expression agains the XML
	 * document and generate a result
	 */
	public NodeList getNodes(String xpathExpression, String xml, String encoding) throws ParserConfigurationException, SAXException, IOException, XPathExpressionException {
		Document doc = buildDocument(xml, encoding);
		XPathExpression expr = buildXPathExpression(xpathExpression);

	    Object result = expr.evaluate(doc, XPathConstants.NODESET);
	    return (NodeList) result;
	    
	}
	
	/**
	 * Method to extract data from a Push XML stream
	 * Receives an XPath expression as input an returns a single result 
	 */
	public String singleAccess(String xpathExpression, String xml, String encoding) throws ParserConfigurationException, SAXException, IOException, XPathExpressionException {
		NodeList nodes = getNodes(xpathExpression, xml, encoding);
		if(nodes.getLength()==1) {
			return nodes.item(0).getNodeValue();
		}
		return null;
	}
	
	/**
	 * Method to extract data from a Push XML stream
	 * Receives an XPath expression as input an returns multiple results 
	 */
	public ArrayList<String> multiAccess(String xpathExpression, String xml, String encoding) throws ParserConfigurationException, SAXException, IOException, XPathExpressionException {
		NodeList nodes = getNodes(xpathExpression, xml, encoding);
		ArrayList<String> res = new ArrayList<String>();
		for (int i = 0; i < nodes.getLength(); i++) {	        
	        res.add(nodes.item(i).getNodeValue());
	    }
	    return res;
	}
}