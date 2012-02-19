package com.cesarcd.tests.unit;

import java.io.IOException;
import java.util.Properties;

import org.junit.*;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;
import org.xml.sax.SAXException;

import com.cesarcd.tests.clients.WAPPlayer;
import com.cesarcd.tests.util.Constants;
import com.cesarcd.tests.util.PropsUtils;
import com.meterware.httpunit.WebResponse;

import static org.junit.Assert.*;

/**
 * Perform tests as WAP client
 */
@RunWith(SpringJUnit4ClassRunner.class)
@ContextConfiguration(locations={"all-context.xml"})
public class WAPTests {
	private Properties props;
	@Autowired private PropsUtils propsUtil;
	
	@Before
	public void setUp() throws Exception {
		props = PropsUtils.load(Constants.PROPS_PATH);
	}
	
	@Test
	public void test_wapLanding() throws IOException, SAXException {
		WAPPlayer player = new WAPPlayer();
		WebResponse resp = player.send(props.getProperty("landing.wap.url"));
		assertFalse( "Found wifi Message", resp.getText().contains(props.getProperty("wifi.warning")) );
	}

	public PropsUtils getPropsUtil() {
		return propsUtil;
	}

	public void setPropsUtil(PropsUtils propsUtil) {
		this.propsUtil = propsUtil;
	}
}
