package com.cesarcd.tests.unit;

import java.io.IOException;
import java.util.Properties;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import javax.xml.parsers.ParserConfigurationException;
import javax.xml.xpath.XPathExpressionException;

import org.junit.*;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;
import org.xml.sax.SAXException;

import com.cesarcd.tests.clients.JavaPlayer;
import com.cesarcd.tests.clients.LicenseRenewalJavaPlayer;
import com.cesarcd.tests.util.Constants;
import com.cesarcd.tests.util.PropsUtils;
import com.cesarcd.tests.util.TestUtil;
import com.meterware.httpunit.WebLink;
import com.meterware.httpunit.WebResponse;

import static org.junit.Assert.*;

/**
 * Perform tests as Android/RIM Client
 */
@RunWith(SpringJUnit4ClassRunner.class)
@ContextConfiguration
public class BasicPlayerTests {
	private Properties props;
	@Autowired private PropsUtils propsUtil;
	@Autowired private JavaPlayer player;
	@Autowired private LicenseRenewalJavaPlayer licPlayer;

	@Before
	public void setUp() throws Exception {
		props = PropsUtils.load(Constants.PROPS_PATH);
	}
	
	@Test
	public void test_playerLanding() throws IOException, SAXException {
        WebResponse resp = player.send(props.getProperty("landing.url"));
		assertFalse( "Found wifi Message", resp.getText().contains(props.getProperty("wifi.warning")));
	}
	
	/* Test the purchase workflow, including fetching
	 * content from the Push XML and validating MIME
	 * type response
	 */
	@Test(timeout=30000)
	public void test_purchase() throws IOException, SAXException, XPathExpressionException, ParserConfigurationException {
		WebResponse resp = player.send(props.getProperty("landing.url"));

		WebLink link2Track = TestUtil.getLinkByURLPattern(resp.getLinks(), "track.xhtml");
		resp = player.send(link2Track.getRequest());

		WebLink buyLink = TestUtil.getLinkByURLPattern(resp.getLinks(), "trackconfirm.xhtml");
		resp = player.send(buyLink.getRequest());

		WebLink purchaseLink = TestUtil.getLinkByURLPattern(resp.getLinks(), "purchase.xhtml");
		resp = player.send(purchaseLink.getRequest());

		assertTrue(resp.getText(), resp.getText().contains("<push") );
		assertTrue(resp.getText().contains("<file") );
		
		String contentUrl = TestUtil.extractContentUrl(resp.getText());
		assertTrue(contentUrl.contains("urmusic.ca/NODRM/"));

		WebResponse respContent = player.sendHead(contentUrl);

		assertEquals(200, 			respContent.getResponseCode());
		assertEquals("OK", 			respContent.getResponseMessage());
		
		if (contentUrl.contains(".mp3")) 
			assertEquals("audio/mp3", 	respContent.getContentType());
		else if (contentUrl.contains(".aac")) 
			assertEquals("audio/aac", 	respContent.getContentType());
	}
	
	@Test(timeout=30000)
	public void test_rental() throws IOException, SAXException, XPathExpressionException, ParserConfigurationException {
		WebResponse resp = player.send(props.getProperty("landing.url"));

		WebLink link2Track = TestUtil.getLinkByURLPattern(resp.getLinks(), "track.xhtml");
		resp = player.send(link2Track.getRequest());

		WebLink purchaseLink = TestUtil.getLinkByURLPattern(resp.getLinks(), "trackdownload.xhtml");
		resp = player.send(purchaseLink.getRequest());
		rentalContentCheck(resp.getText());
	}

	/* Test the rental workflow, including fetching
	 * content from the Push XML and validating MIME
	 * type response
	 */
	@Test(timeout=30000)
	public void test_prelisten() throws XPathExpressionException, ParserConfigurationException, IOException, SAXException {
		WebResponse resp = player.send(props.getProperty("landing.url"));

		WebLink link2Track = TestUtil.getLinkByURLPattern(resp.getLinks(), "track.xhtml");
		resp = player.send(link2Track.getRequest());

		WebLink previewLink = resp.getLinkWith("Preview Track");
		WebResponse respPreview = player.send(previewLink.getRequest());

		assertTrue(respPreview.getText().contains("<push") );
		assertTrue(respPreview.getText().contains("<file") );

		String prelistenUrl = TestUtil.extractContentUrl(respPreview.getText());

		assertTrue(prelistenUrl.contains("urmusic.ca/Prelisten/encoding/"));

		WebResponse respContent = player.sendHead(prelistenUrl);

		assertEquals(200, 			respContent.getResponseCode());
		assertEquals("OK", 			respContent.getResponseMessage());
		assertEquals("audio/aac", 	respContent.getContentType());
	}
	
	@Test(timeout=30000)
	public void test_Lacq() throws XPathExpressionException, ParserConfigurationException, IOException, SAXException {
		WebResponse resp = player.send(props.getProperty("license.acquisition.url"));
		rentalContentCheck(resp.getText());
	}
	
	@Test
	public void test_licenseRenewal() throws IOException, SAXException, XPathExpressionException, ParserConfigurationException {
        WebResponse resp = licPlayer.send(props.getProperty("landing.url"));
        String licenseUrl = TestUtil.extractSubscriptionUrl(resp.getText());

        assertTrue(licenseUrl.contains("//urmusic.ca"));
        assertTrue(licenseUrl.contains("master.dat"));
        
        Pattern p = Pattern.compile("http://urmusic.ca/SDC/[0-9]+/[0-9]+/master.dat");
        Matcher m = p.matcher(licenseUrl);
        assertTrue(m.find());
	}

	@Test
	public void testAlbumDeepLink() throws IOException, SAXException {
        WebResponse resp = player.send(props.getProperty("album.deep.link"));
		assertTrue(resp.getText().contains("album-item"));
	}
	
	/* 
	 * Check all metadata values related to a 
	 * download via subscription
	 */
	private void rentalContentCheck(String content) throws XPathExpressionException, ParserConfigurationException, SAXException, IOException {
		assertTrue(content.contains("<push"));
		assertTrue(content.contains("<file"));
		
		String contentUrl = TestUtil.extractContentUrl(content);
		assertTrue(contentUrl.contains("example.com/MUS/"));
		assertTrue(contentUrl.contains(".mus"));

		WebResponse respContent = player.sendHead(contentUrl);

		assertEquals(200, respContent.getResponseCode());
		assertEquals("OK", respContent.getResponseMessage());		 
		assertEquals("application/com.abc.cde3", respContent.getContentType());
	}

	public PropsUtils getPropsUtil() {
		return propsUtil;
	}

	public void setPropsUtil(PropsUtils propsUtil) {
		this.propsUtil = propsUtil;
	}

	public LicenseRenewalJavaPlayer getLicPlayer() {
		return licPlayer;
	}

	public void setLicPlayer(LicenseRenewalJavaPlayer licPlayer) {
		this.licPlayer = licPlayer;
	}

	public JavaPlayer getPlayer() {
		return player;
	}

	public void setPlayer(JavaPlayer player) {
		this.player = player;
	}
}
